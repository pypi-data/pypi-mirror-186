from __future__ import annotations
import logging
import typing
from datetime import datetime
from dateutil.relativedelta import relativedelta
import asyncio
from enum import Enum
from dataclasses import dataclass
import pyaware.commands
from pathlib import Path
from pyaware import events, async_threaded, runtime_logger
from pyaware.triggers.process import run_triggers
from pyaware.protocol.imac2 import commands, ModuleStatus
from pyaware.data_types.modbus import (
    AddressMapUint16,
    Param,
    ParamBits,
    ParamMask,
    ParamMaskBool,
    ParamMaskScale,
    ParamCType,
)
from pyaware.store import memory_storage
from pyaware.mqtt.models import TopologyChildren
from pyaware.data_types.common import WrappableDict
import pyaware.aggregations
from pyaware import watchdog
from typing import Dict, Set, Awaitable, Callable

if typing.TYPE_CHECKING:
    from pyaware.controllers.imac2.master import Imac2MasterController

log = logging.getLogger(__file__)


class Units(Enum):
    percent = 0
    ppm = 1


number = typing.Union[int, float]


@dataclass
class Detector:
    symbol: str
    type: str
    units: str
    span: number
    zero: number = 0

    def __post_init__(self):
        self.fault_ranges = {
            2800: "detector-low-soft-fault",
            3000: "detector-low-warmup",
            3200: "detector-under-range",
            20800: "detector-over-range",
            21000: "detector-high-warmup",
            21200: "detector-high-soft-fault",
        }
        self.base_faults = {
            "detector-low-soft-fault": False,
            "detector-low-warm-up": False,
            "detector-under-range": False,
            "detector-over-range": False,
            "detector-high-warm-up": False,
            "detector-high-soft-fault": False,
        }
        if self.type == "infra-red":
            self.fault_ranges[3700] = "detector-ndir-zero-shift-neg"
            self.base_faults["detector-ndir-zero-shift-neg"] = False

    def decode(self, data: number) -> dict:
        faults = self.base_faults.copy()
        try:
            faults[self.fault_ranges[data]] = True
        except KeyError:
            pass
        decoded = {
            "detector-units": self.units,
            "detector-zero": self.zero,
            "detector-span": self.span,
            "detector-symbol": self.symbol,
            "detector-sensor-type": self.type,
        }
        if self.type != "unknown":
            decoded["detector-gas-value"] = (
                (data - 4000) / 16000 * (self.span + self.zero)
            )
        if any(faults.values()):
            decoded["detector-gas-analog-safe-gas"] = -2000
        else:
            decoded["detector-gas-analog-safe-gas"] = data
        decoded.update(faults)
        return decoded


@events.enable
class ImacModule:
    specs: dict = None
    name: str = "Unknown iMAC Module"
    blocks: typing.List[int] = [0]
    module_type: str = "imac-module-unknown"
    config_name: str = "imac_module_parameter_spec.yaml"
    starting_params: typing.List[str] = []
    online_address_params: typing.List[str] = []
    rollcall_address_params: typing.List[str] = []

    def __init__(self, controller: Imac2MasterController, dev_id=""):
        self.controller = controller
        self.protocol = controller.protocol
        self.config_path = (
            Path(pyaware.__file__).parent
            / "devices"
            / "ampcontrol"
            / "imac"
            / self.config_name
        )
        self.config = pyaware.config.load_yaml_config(self.config_path)
        self.parameters = {"poll": {}, "block": {}}
        self.current_state = WrappableDict(**{"dev-id": dev_id})
        self.last_poll_read: datetime = datetime.utcfromtimestamp(0)
        self.store_state = WrappableDict()
        self.send_state = WrappableDict()
        self.event_state = WrappableDict()
        self.commands = pyaware.commands.Commands(
            {
                "set-imac-address": [
                    pyaware.commands.ValidateIn(range(256)),
                    commands.WriteParam("address-single"),
                    commands.ReadParam("address-single"),
                    commands.ValidateParam("address-single"),
                    commands.UpdateMeta("address-single"),
                    commands.UpdateSpecs(),
                ],
                "set-parameters": [commands.SetParameters()],
                "get-parameters": [commands.GetParameters()],
            },
            meta_kwargs={"imac_module": self},
        )
        self.store_timestamp = datetime.utcfromtimestamp(0)
        self.send_timestamp = datetime.utcfromtimestamp(0)
        self.triggers = pyaware.triggers.build_from_device_config(
            self.config_path,
            device_id=dev_id,
            send_state=self.send_state,
            store_state=self.store_state,
            event_state=self.event_state,
            current_state=self.current_state,
        )
        self.aggregates = pyaware.aggregations.build_from_device_config(
            self.config_path
        )
        self.parameter_handlers: Dict[str, Callable[[Set], Awaitable[dict]]] = {
            "block": self.parameter_block_reader
        }
        log.info(
            f"Adding device schedule {self.module_type} - {self.current_state['dev-id']}"
        )
        log.info(f"Adding collect triggers {self.triggers.get('collect', {})}")
        self.setup_watchdogs()
        self.schedule_reads()

    def setup_watchdogs(self):
        # Do not set up block read watchdogs for modules that do not have block reads (eg RTS)
        if self.module_type == "imac-controller-rts":
            return

        dog_block = watchdog.WatchDog(
            100000,  # All modules should read at least once per day. Give a bit of extra time due to bus loading
            lambda: None,
            lambda: asyncio.create_task(self.check_connected()),
        )
        watchdog.manager.add(
            f"imac_module_block_{self.current_state['dev-id']}", dog_block
        )
        self.read_parameter_block = watchdog.watch(
            f"imac_module_block_{self.current_state['dev-id']}", starve_on_exception=1
        )(self.read_parameter_block)
        self.write_parameter_block = watchdog.watch(
            f"imac_module_block_{self.current_state['dev-id']}", starve_on_exception=1
        )(self.write_parameter_block)
        dog_block.start(start_fed=True)

    async def remove_watchdogs(self):
        # Do not set up block read watchdogs for modules that do not have block reads (eg RTS)
        if self.module_type == "imac-controller-rts":
            return

        await watchdog.manager.remove(
            f"imac_module_block_{self.current_state['dev-id']}"
        )

    async def check_connected(self):
        """
        Checks if the module is still connected by checking block 0. Calls protocol directly to avoid the watchdog
        recursing
        :return:
        """
        try:
            await self.protocol.read_by_serial_number(
                self.current_state["serial_number"],
                self.current_state["generation_id"],
                0,
            )
        except (IOError, ValueError):
            log.info(f"Check connected failed for {self.current_state['dev-id']}")
            events.publish("remove_devices", devices=[self.current_state["dev-id"]])

    def schedule_reads(self):
        self.controller.schedule_reads.update(
            self._format_schedule_reads(self.triggers["collect"].get("block", []))
        )

    def _format_schedule_reads(self, schedule: list):
        return {f"{itm.device}::{itm.param}": itm for itm in schedule}

    @events.subscribe(topic="imac_module_data")
    async def process_module_data_triggers(self, data, timestamp):
        dev_data = data.get(self.current_state["dev-id"])
        if dev_data is None:
            return
        event_data = await run_triggers(
            self.triggers.get("process", {}).get("event", {}), dev_data, timestamp
        )
        if runtime_logger.triggers:
            log.debug(
                f"Event triggers {event_data} on {self.current_state['dev-id']}: {data}"
            )

        if event_data:
            futs = []
            for param, value in event_data.items():
                futs.append(
                    events.publish(
                        f"parameter_trigger/{self.current_state['dev-id']}/{param}",
                        data=next(iter(value.values())),
                        timestamp=timestamp,
                    ).all()
                )
            self.event_state.update(event_data)
            results = await asyncio.gather(*futs)
            for res in results:
                if res is not None:
                    for itm in res:
                        if isinstance(itm, dict):
                            dev_data.update(itm)

        store_data, send_data = await asyncio.gather(
            run_triggers(
                self.triggers.get("process", {}).get("store", {}), dev_data, timestamp
            ),
            run_triggers(
                self.triggers.get("process", {}).get("send", {}), dev_data, timestamp
            ),
        )
        if runtime_logger.triggers:
            log.debug(
                f"Store triggers {store_data} on {self.current_state['dev-id']}: {data}"
            )
            log.debug(
                f"Send triggers {send_data} on {self.current_state['dev-id']}: {data}"
            )

        if store_data:
            memory_storage.update(
                store_data,
                topic=f"{self.controller.device_id}/{self.current_state['dev-id']}",
            )
            self.update_store_state(store_data)
        if send_data:
            memory_storage.update(
                send_data,
                topic=f"{self.controller.device_id}/{self.current_state['dev-id']}",
            )
            cached_data = memory_storage.pop(
                f"{self.controller.device_id}/{self.current_state['dev-id']}"
            )
            aggregated_data = pyaware.aggregations.aggregate(
                cached_data, self.aggregates
            )
            events.publish(
                f"trigger_send",
                data=aggregated_data,
                meta=self.dict(),
                timestamp=timestamp,
                topic_type="telemetry_serial",
                device_id=self.controller.device_id,
                serial_number=self.controller.serial_number,
            )
            self.update_send_state(cached_data)

    def update_specs(self):
        self.current_state.update(
            pyaware.data_types.resolve_static_data_types(
                self.config["parameters"], self.current_state
            )
        )
        self.parameters.update(
            pyaware.data_types.parse_data_types_by_source(
                self.config["parameters"], self.current_state
            )
        )

    def update_from_roll_call(
        self, serial_number, generation_id, imac_address, version, module_type, **kwargs
    ):
        """
        Check if the module is the same as last roll call, if no then update internal representation
        :param serial_number:
        :param generation_id:
        :param imac_address:
        :param version:
        :param module_type:
        :return:
        """
        new_params = {
            "serial_number": serial_number,
            "generation_id": generation_id,
            "address-single": imac_address,
            "module_type": module_type,
            "version": version,
            "software_version": (version & 0xF00) >> 8,
            "hardware_version": (version & 0xF000) >> 12,
            "dev-id": f"{serial_number}-G{generation_id + 1}",
        }

        self.current_state.update(new_params)
        events.publish(
            "imac_module_data",
            data={self.current_state["dev-id"]: new_params},
            timestamp=datetime.utcnow(),
        )
        self.update_specs()
        for trig in self.triggers.get("collect", {}).get("read", []):
            try:
                trig.device = self.current_state["dev-id"]
            except AttributeError:
                pass

    def __repr__(self):
        return (
            f"{self.name} <Serial {self.current_state.get('serial_number')}"
            f"-G{self.current_state.get('generation_id', -2) + 1} "
            f"@ address {self.current_state.get('address-single')}>"
        )

    async def read_all_parameters(self):
        parameters = {}
        for block in self.blocks:
            addr_map = await self.read_parameter_block(block)
            for spec in self.parameters["block"].values():
                parameters.update(spec.decode(addr_map, block))
        return parameters

    async def parameter_block_reader(self, data: set) -> dict:
        blocks = {
            spec.block
            for spec in self.parameters["block"].values()
            if spec.keys().intersection(data)
        }
        parameters = {}
        for block in blocks:
            try:
                addr_map = await self.read_parameter_block(block)
                for spec in self.parameters["block"].values():
                    parameters.update(spec.decode(addr_map, block))
            except (ValueError, IOError):
                log.error(
                    f"Failed to read {self.current_state['dev-id']}: block {block}"
                )
        return parameters

    async def read_parameter_block(self, block):
        return await self.protocol.read_by_serial_number(
            self.current_state["serial_number"],
            self.current_state["generation_id"],
            block,
        )

    async def write_parameter_block(self, block, addr_map: AddressMapUint16):
        await self.protocol.write_by_serial_number(
            self.current_state["serial_number"],
            self.current_state["generation_id"],
            block,
            addr_map,
        )

    async def write_parameter_block_no_check(self, block, addr_map: AddressMapUint16):
        await self.protocol.write_by_serial_number_no_check(
            self.current_state["serial_number"],
            self.current_state["generation_id"],
            block,
            addr_map,
        )

    async def write_parameters(self, data: dict):
        """
        :param data: Dictionary of form parameter: value
        :return:
        """
        blocks = {
            spec.block
            for spec in self.parameters["block"].values()
            if spec.keys().intersection(data.keys())
        }
        for block in blocks:
            addr_map = await self.read_parameter_block(block)
            addr_map = self.build_parameter_writes(data, addr_map, block)
            await self.write_parameter_block(block, addr_map)

    async def write_parameters_no_check(self, data: dict):
        """
        :param data: Dictionary of form parameter: value
        :return:
        """
        blocks = {
            spec.block
            for spec in self.parameters["block"].values()
            if spec.keys().intersection(data.keys())
        }
        for block in blocks:
            addr_map = await self.read_parameter_block(block)
            addr_map = self.build_parameter_writes(data, addr_map, block)
            await self.write_parameter_block_no_check(block, addr_map)

    async def read_parameters(self, data: set) -> dict:
        """
        :param data: A set of parameter values to read
        :param exact: If true will only return the parameters that were in the original data set
        :return:
        """
        parameters = {}
        # Clear send triggers for all requested parameters
        for key in data:
            self.send_state.pop(key, None)
        for source in self.parameters.copy():
            handler = self.parameter_handlers.get(source)
            if handler is not None:
                parameters.update(await handler(data))
        timestamp = datetime.utcnow()
        # Schedule parameters that failed to read for 10 minutes (ignoring pre-set deadlines)
        self.update_deadline_state(data - parameters.keys(), 600)
        # Updated the parameters read timestamps to schedule for the associated deadline
        self.update_read_state(set(parameters), timestamp)
        self.current_state.update(parameters)
        events.publish(
            "imac_module_data",
            data={self.current_state["dev-id"]: parameters},
            timestamp=timestamp,
        )
        self.update_specs()
        return parameters

    def build_parameter_writes(
        self, data: dict, addr_map: AddressMapUint16, block: int
    ) -> AddressMapUint16:
        """
        Builds up the data to be written in
        :return: Updated address map
        """
        for spec in self.parameters["block"].values():
            if spec.block == block:
                spec.encode(data, addr_map)
        return addr_map

    def _process_module_scan_data(self, addr_map: AddressMapUint16, parameters: dict):
        processed = {}
        for param_spec in parameters.values():
            if isinstance(param_spec.address, int):
                addresses = [param_spec.address]
            else:
                addresses = param_spec.address
                if addresses is None:
                    addresses = []
            for addr in addresses:
                if 0 < addr < 0x100 and self.protocol.parse_status(
                    addr_map[addr + 0x100]
                ) in [ModuleStatus.ONLINE, ModuleStatus.SYSTEM]:
                    processed.update(
                        {k: v for k, v in param_spec.decode(addr_map).items()}
                    )
        return processed

    def _process_module_data_by_params(
        self, addr_map: AddressMapUint16, parameters: dict
    ):
        processed = {}
        for param_spec in parameters.values():
            if isinstance(param_spec.address, int):
                addresses = [param_spec.address]
            else:
                addresses = param_spec.address
                if addresses is None:
                    addresses = []
            for addr in addresses:
                if (
                    addr > 0x100
                    or addr == 0
                    or self.protocol.parse_status(addr_map[addr + 0x100])
                    in [ModuleStatus.ONLINE, ModuleStatus.SYSTEM]
                    or param_spec.meta.get("ignore-status")
                ):
                    processed.update(
                        {k: v for k, v in param_spec.decode(addr_map).items()}
                    )
        return processed

    @async_threaded
    def process_module_data(
        self, addr_map: AddressMapUint16, timestamp: datetime = None
    ):
        """
        Porcesses the module data from an address map to determine the valid parameter data from the module
        :param addr_map:
        :param timestamp:
        :return:
        """
        parameters = self._process_module_scan_data(addr_map, self.parameters["poll"])
        # Parameters poll == 0 indicates it is an output module.
        # Should still process the remaining parameters as this is not a valid offline condition for the output modules
        if parameters or len(self.parameters["poll"]) == 0:
            self.last_poll_read = datetime.utcnow()
            # Only process any poll data that doesn't directly live in module scan addresses
            poll_missing_params = {
                k: v
                for k, v in self.parameters.get("poll", {}).items()
                if k in set(self.parameters.get("poll", {})).difference(parameters)
            }
            parameters.update(
                self._process_module_data_by_params(addr_map, poll_missing_params)
            )
            # Process data that is external to the device (eg bypass di4 for gg2) but may live within module scan address
            parameters.update(
                self._process_module_data_by_params(
                    addr_map, self.parameters.get("external", {})
                )
            )
            # Process any static data that may be present only if there is valid poll data
            parameters.update(
                {
                    param: self.current_state.get(param)
                    for param in self.parameters.get("static", {})
                    if param in self.current_state
                }
            )

        return parameters

    def diff_module_data(self, parameters: dict):
        """
        Compare a subset of parameter values against the module state
        :param parameters:
        :return:
        """
        return {
            k: parameters[k]
            for k in parameters
            if self.current_state.get(k) != parameters[k]
        }

    def update_current_state(self, parameters: dict):
        """
        Update the state used to run diff module data against
        :param parameters: Parameter dictionary to update the state
        :return:
        """
        self.current_state.update(parameters)

    def update_store_state(self, parameters: dict):
        """
        Update the state the module has represented in the cache database
        :param parameters: Parameter dictionary to update the state
        :return:
        """
        self.store_state.update(parameters)

    def update_send_state(self, parameters: dict):
        """
        Update the state used the module has represented from queued mqtt messages
        :param parameters: Parameter dictionary to update the state
        :return:
        """
        self.send_state.update(parameters)

    def update_read_state(self, parameters: set, timestamp: datetime):
        """
        Update the timestamp since the last read parameters
        :param parameters: Parameter dictionary to update the state
        :return:
        """
        for param in parameters:
            try:
                collect_trig = self.controller.schedule_reads[
                    f"{self.current_state['dev-id']}::{param}"
                ]
                self.controller.schedule_reads[
                    f"{self.current_state['dev-id']}::{param}"
                ] = collect_trig._replace(
                    deadline=datetime.utcnow()
                    + relativedelta(seconds=collect_trig.time_delta)
                )
            except KeyError:
                continue

    def update_deadline_state(self, parameters: set, seconds: int):
        """
        Update the timestamp since the last read parameters
        :param parameters: Parameter dictionary to update the state
        :return:
        """
        for param in parameters:
            try:
                collect_trig = self.controller.schedule_reads[
                    f"{self.current_state['dev-id']}::{param}"
                ]
                self.controller.schedule_reads[
                    f"{self.current_state['dev-id']}::{param}"
                ] = collect_trig._replace(
                    deadline=datetime.utcnow() + relativedelta(seconds=seconds)
                )
            except KeyError:
                continue

    def reset_deadline_state(self, parameters: set):
        """
        Resets the timestamp since the last read parameters. Making the parameters to high priority
        (10 seconds from utc 1/1/1970 leaving room for other potentially higher priority parameters)
        :param parameters: Parameter dictionary to update the state
        :return:
        """
        for param in parameters:
            try:
                collect_trig = self.controller.schedule_reads[
                    f"{self.current_state['dev-id']}::{param}"
                ]
                self.controller.schedule_reads[
                    f"{self.current_state['dev-id']}::{param}"
                ] = collect_trig._replace(deadline=datetime.utcfromtimestamp(10))
            except KeyError:
                continue

    def update_event_state(self, parameters: dict):
        """
        Update the state used the module has represented from queued mqtt messages
        :param parameters: Parameter dictionary to update the state
        :return:
        """
        self.event_state.update(parameters)

    def identify_online_addresses(self) -> dict:
        return {
            param: self.current_state[param]
            for param in self.online_address_params
            if param in self.current_state
        }

    def identify_rollcall_addresses(self) -> dict:
        return {
            param: self.current_state[param]
            for param in self.rollcall_address_params
            if param in self.current_state
        }

    async def disconnect(self):
        self.controller.remove_device_from_schedule(self.current_state["dev-id"])
        try:
            del self.commands.meta_kwargs
        except AttributeError:
            pass
        self.parameter_handlers.clear()
        await self.remove_watchdogs()
        events.disable_object(id(self))

    def identify(self):
        response = TopologyChildren(
            values=self.identify_rollcall_addresses(),
            type=self.module_type,
            serial=self.current_state.get("dev-id"),
            children=[],
        )
        return response

    def dict(self):
        response = {"type": self.module_type}
        if self.current_state.get("dev-id"):
            response["serial"] = self.current_state.get("dev-id")
        return response

    async def find_missing_starting_data(self):
        missing = {k for k in self.starting_params if self.current_state.get(k) is None}
        if missing:
            for _ in range(2):
                params = await self.read_parameters(missing)
                if params:
                    break
                else:
                    log.warning(
                        f"Failed to read {self.name} {self.current_state['dev-id']} starting parameters"
                    )
            self.current_state.update(params)
            self.update_specs()

    def any_addresses_online(self, address_status: typing.List[ModuleStatus]) -> bool:
        """
        Checks that any addresses for the device are online.
        This can be used to determine if a module can be safely deleted on a failed roll call
        :param address_status: The address status of the imac bus
        :return:
        """
        online_addresses = {
            i for i, x in enumerate(address_status) if x == ModuleStatus.ONLINE
        }
        return bool(
            online_addresses.intersection(
                set(self.identify_online_addresses().values())
            )
        )


class RtsModule(ImacModule):
    name = "Rts Module"
    module_type = "imac-controller-rts"
    config_name = "rts_parameter_spec.yaml"
    rollcall_address_params = [
        "l1-address-rts-config-0",
        "l1-address-rts-config-1",
        "l1-address-rts-config-2",
    ]

    def __init__(self, *args, **kwargs):
        super(RtsModule, self).__init__(*args, **kwargs)
        self.commands.update(
            {
                "remote-bypass": [
                    pyaware.commands.ValidateIn(range(2)),
                    pyaware.commands.TopicTask(
                        f"remote_bypass/{id(self)}", {"data": "value"}
                    ),
                ],
                "remote-trip": [
                    pyaware.commands.ValidateIn(range(2)),
                    pyaware.commands.TopicTask(
                        f"remote_trip/{id(self)}", {"data": "value"}
                    ),
                ],
            }
        )

    @events.subscribe(topic="remote_bypass/{id}")
    async def remote_bypass(self, data):
        await self.protocol.write_bit(
            0x52A, self.current_state["logical-number"] - 1, data
        )

    @events.subscribe(topic="remote_trip/{id}")
    async def remote_trip(self, data):
        await self.protocol.write_bit(
            0x52B, self.current_state["logical-number"] - 1, data
        )

    def update_from_roll_call(self, imac_address, dev_id, **kwargs):
        """
        Check if the module is the same as last roll call, if no then update internal representation
        :param imac_address:
        :param dev_id:
        :return:
        """
        schema = self.controller.address_schema_match(imac_address)
        if schema["name"] not in ["rts-config-0", "rts-config-1", "rts-config-2"]:
            log.info(f"Schema Violation: RTS address {imac_address} not in schema")
        _, fieldbus_address, logical_number = dev_id.split("-")
        new_params = {
            f"address-{schema['name']}": imac_address,
            "dev-id": dev_id,
            "master-fieldbus-number": int(fieldbus_address),
            "logical-number": int(logical_number),
        }
        self.current_state.update(new_params)
        self.update_specs()
        events.publish(
            "imac_module_data",
            data={self.current_state["dev-id"]: new_params},
            timestamp=datetime.utcnow(),
        )

    async def check_connected(self):
        """
        If the RTS is checking it is connected. Then it isn't connected as this method is only called if it did not
        find the RTS
        recursing
        :return:
        """
        log.info(
            f"RTS {self.current_state['dev-id']} detected as disconnected. Removing"
        )
        events.publish("remove_devices", devices=[self.current_state["dev-id"]])


@events.enable
class Di4(ImacModule):
    name = "DI4 Module"
    module_type = "imac-module-di4"
    config_name = "di4_parameter_spec.yaml"
    starting_params = [f"invert-status-{x}" for x in range(1, 5)]
    online_address_params = ["address-single"]
    rollcall_address_params = ["address-single"]

    def __init__(self, *args, **kwargs):
        super(Di4, self).__init__(*args, **kwargs)
        dev_id = self.current_state["dev-id"]
        events.subscribe(
            self.update_io_feedback,
            topic=f"parameter_trigger/{dev_id}/switch-status-raw-1",
            parent=self,
        )
        events.subscribe(
            self.update_io_feedback,
            topic=f"parameter_trigger/{dev_id}/switch-status-raw-2",
            parent=self,
        )
        events.subscribe(
            self.update_io_feedback,
            topic=f"parameter_trigger/{dev_id}/switch-status-raw-3",
            parent=self,
        )
        events.subscribe(
            self.update_io_feedback,
            topic=f"parameter_trigger/{dev_id}/switch-status-raw-4",
            parent=self,
        )
        events.subscribe(
            self.update_io_feedback,
            topic=f"parameter_trigger/{dev_id}/invert-status-1",
            parent=self,
        )
        events.subscribe(
            self.update_io_feedback,
            topic=f"parameter_trigger/{dev_id}/invert-status-2",
            parent=self,
        )
        events.subscribe(
            self.update_io_feedback,
            topic=f"parameter_trigger/{dev_id}/invert-status-3",
            parent=self,
        )
        events.subscribe(
            self.update_io_feedback,
            topic=f"parameter_trigger/{dev_id}/invert-status-4",
            parent=self,
        )

    def update_io_feedback(self, data, timestamp):
        try:
            resp = {
                f"switch-status-{x}": self.current_state[f"switch-status-raw-{x}"]
                ^ self.current_state[f"invert-status-{x}"]
                for x in range(1, 5)
            }
        except KeyError:
            return
        events.publish(
            "imac_module_data",
            data={f"{self.current_state['dev-id']}": resp},
            timestamp=timestamp,
        )


@events.enable
class Lim(ImacModule):
    name = "LIM Module"
    module_type = "imac-module-lim"
    config_name = "lim_parameter_spec.yaml"
    starting_params = ["mode"]
    online_address_params = ["address-single"]
    rollcall_address_params = ["address-single"]


@events.enable
class SimP(ImacModule):
    name = "SIM-P Module"
    module_type = "imac-module-sim-p"
    config_name = "simp_parameter_spec.yaml"
    starting_params = ["modbus-start-address", "modbus-register-count"]
    online_address_params = ["address-single"]
    rollcall_address_params = ["address-single"]

    def update_specs(self):
        super(SimP, self).update_specs()
        address = int(self.current_state.get("address-single", 0))
        register_count = int(self.current_state.get("modbus-register-count", 0))
        if address:
            if register_count:
                self.parameters["poll"].update(
                    {
                        f"raw-word-{x}": Param(address + x + 1, f"raw-word-{x}")
                        for x in range(register_count)
                    }
                )

    def identify_online_addresses(self) -> dict:
        addrs = super().identify_online_addresses()
        addrs.update(
            {
                param.idx: param.address
                for param in self.parameters["poll"].values()
                if param.idx.startswith("raw-word")
            }
        )
        return addrs


@events.enable
class Rtd1(ImacModule):
    name = "RTD-1 Module"
    module_type = "imac-module-rtd1"
    config_name = "rtd1_parameter_spec.yaml"
    types = {54: "flags", 55: "temp"}
    starting_params = [
        "voltage-l1",
        "set-point-low",
        "set-point-high",
        "address-flags",
        "address-temp",
    ]
    online_address_params = ["address-flags", "address-temp"]
    rollcall_address_params = ["address-flags"]


@events.enable
class SimT(ImacModule):
    name = "SIM-T Module"
    module_type = "imac-module-sim-t"
    online_address_params = ["address-single"]
    rollcall_address_params = ["address-single"]


@events.enable
class SimG(ImacModule):
    name = "SIM-G Module"
    module_type = "imac-module-sim-g"
    config_name = "simg_parameter_spec.yaml"
    online_address_params = ["address-single"]
    rollcall_address_params = ["address-single"]


@events.enable
class Aim(ImacModule):
    name = "Aim Module"
    module_type = "imac-module-aim"
    config_name = "aim_parameter_spec.yaml"
    starting_params = ["address-flags", "address-analog", "address-power"]
    types = {48: "flags", 49: "analog", 50: "power"}
    blocks = [0, 1, 2]
    online_address_params = ["address-flags", "address-analog", "address-power"]
    rollcall_address_params = ["address-flags"]


@events.enable
class Ro4(ImacModule):
    name = "RO4 Module"
    module_type = "imac-module-ro4"
    config_name = "ro4_parameter_spec.yaml"
    starting_params = [f"invert-status-{x}" for x in range(1, 5)]
    online_address_params = ["address-single"]
    rollcall_address_params = ["address-single"]


@events.enable
class Do4(ImacModule):
    name = "DO4 Module"
    module_type = "imac-module-do4"
    config_name = "ro4_parameter_spec.yaml"
    starting_params = [f"invert-status-{x}" for x in range(1, 5)]
    online_address_params = ["address-single"]
    rollcall_address_params = ["address-single"]


@events.enable
class Do44(ImacModule):
    name = "DO4-4 Module"
    module_type = "imac-module-do4-4"
    config_name = "do4_4_parameter_spec.yaml"
    starting_params = [f"invert-state-output-{x}" for x in range(1, 5)]
    online_address_params = ["address-output-1"]
    rollcall_address_params = ["address-output-1"]


@events.enable
class Pim(ImacModule):
    name = "PIM Module"
    module_type = "imac-module-pim"
    config_name = "pim_parameter_spec.yaml"
    starting_params = ["set-point-warn", "set-point-trip", "hardware-type"]
    online_address_params = ["address-single"]
    rollcall_address_params = ["address-single"]


@events.enable
class GasGuard2(ImacModule):
    name = "Gasguard 2"
    module_type = "imac-module-gg2"
    config_name = "gasguard2_parameter_spec.yaml"
    types = {61: "flags", 62: "analog", 63: "power"}
    blocks = [0, 1, 2, 3, 4, 5, 6, 7]
    starting_params = [
        "address-flags",
        "address-analog",
        "address-power",
        "address-bypass",
        "detector-type-raw",
        "set-point-1",
        "set-point-2",
        "set-point-3",
    ]
    online_address_params = ["address-flags", "address-analog", "address-power"]
    rollcall_address_params = ["address-flags", "address-analog", "address-power"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_state["detector-type"] = 0
        self.analog_conversion = {
            0: Detector("Unknown", "Unknown", "%", 0, 0),
            1: Detector("CH4", "catalytic", "%", 5, 0),
            2: Detector("CH4", "infra-red", "%", 5, 0),
            3: Detector("CH4", "infra-red", "%", 100, 0),
            4: Detector("CO2", "infra-red", "%", 2, 0),
            5: Detector("CO2", "infra-red", "%", 5, 0),
            6: Detector("CO", "electrochemical", "ppm", 50, 0),
            7: Detector("CO", "electrochemical", "ppm", 100, 0),
            8: Detector("O2", "electrochemical", "%", 25, 0),
            10: Detector("NO2", "electrochemical", "ppm", 10, 0),
            11: Detector("H2S", "electrochemical", "ppm", 50, 0),
            12: Detector("H2S", "electrochemical", "ppm", 100, 0),
        }
        self.parameters["poll"] = {}
        self.commands.update(commands.gasguard_2)
        self.parameters["block"] = {
            "address-flags": ParamMask(0x40E, "address-flags", block=0, mask=0xFF),
            "exception-trigger": Param(0x40F, "exception-trigger", block=0),
            # "catalytic-reset-address": ParamMask(0x410, "catalytic-reset-address", mask=0xff, block=0),
            # "catalytic-reset-command": ParamMask(0x410, "catalytic-reset-command", mask=0xff00, rshift=8, block=0),
            "address-bypass": ParamMask(0x411, "address-bypass", mask=0xFF, block=0),
            "aim-compatibility-mode": ParamMask(
                0x411, "aim-compatibility-mode", mask=0x100, rshift=8, block=0
            ),
            "ui-lockout": ParamMask(0x411, "ui-lockout", mask=0x200, rshift=9, block=0),
            "address-analog": ParamMask(0x40E, "address-analog", block=1, mask=0xFF),
            "set-point-1": Param(0x40F, "set-point-1", block=1),
            "set-point-2": Param(0x410, "set-point-2", block=1),
            "set-point-3": Param(0x411, "set-point-3", block=1),
            "address-power": ParamMask(0x40E, "address-power", block=2, mask=0xFF),
            "hysteresis-config": ParamMask(
                0x411, "hysteresis-config", mask=0b1111 << 12, rshift=12, block=2
            ),
            "healthy-config": ParamMask(
                0x411, "healthy-config", mask=0b111 << 9, rshift=9, block=2
            ),
            "warmup-config": ParamMaskBool(
                0x411, "warmup-config", mask=1 << 8, rshift=8, block=2
            ),
            "address-rtc": ParamMask(0x411, "address-rtc", block=2, mask=0xFF),
            # TODO TBD with Aim mode complicating it for param 2
            "detector-temperature": ParamMaskScale(
                0x40E, "detector-temperature", block=3, scale=0.01
            ),
            "detector-pressure": Param(0x40F, "detector-pressure", block=3),
            "detector-humidity": ParamMaskScale(
                0x410, "detector-humidity", block=3, scale=0.01
            ),
            # "detector-gas-reading-permyriad": Param(0x411, "detector-gas-reading-permyriad", block=3),
            "command-register-code": ParamMask(
                0x411, "command-register-code", mask=0xFF00, rshift=8, block=3
            ),
            "command-register-result": ParamMask(
                0x411, "command-register-result", mask=0xFF, block=3
            ),
            "last-t90-test-result": ParamMaskScale(
                0x40E, "last-t90-test-result", block=4, scale=0.1
            ),
            "last-nata-cal-hours": Param(0x40F, "last-nata-cal-hours", block=4),
            "last-cal-cup-seconds": Param(0x410, "last-cal-cup-seconds", block=4),
            "power-supply-voltage": ParamMaskScale(
                0x411,
                "power-supply-voltage",
                mask=0xFF00,
                rshift=8,
                scale=0.1,
                block=4,
                significant_figures=3,
            ),
            # "misc-flags": ParamBits(0x40f, bitmask={
            #     "bypass_status": 0,
            #     "catalytic-detector-latch": 1,
            #     "detector-warmup": 2
            # }, block=5),
            "postbox-selection": ParamMask(
                0x40E, "postbox-selection", mask=0b111, block=5
            ),
            "detector-type-raw": ParamMask(
                0x40F, "detector-type-raw", mask=0xFF00, rshift=8, block=5
            ),
            "cal-cup-alarm-28-days": ParamMaskBool(
                0x40F, "cal-cup-alarm-28-days", mask=1 << 4, rshift=4, block=5
            ),
            "linearity-test-alarm-14-days": ParamMaskBool(
                0x40F, "linearity-test-alarm-14-days", mask=1 << 3, rshift=3, block=5
            ),
            "linearity-test-last-points": ParamMask(
                0x40F, "linearity-test-last-points", mask=0b111, block=5
            ),
            "postbox-timestamp": ParamCType(
                0x410, "postbox-timestamp", data_type="uint", block=5
            ),
            "detector-serial-number": ParamCType(
                0x40F, "detector-serial-number", data_type="uint", block=6
            ),
            "detector-software-version": Param(
                0x411, "detector-software-version", block=6
            ),
            "display-serial-number": ParamCType(
                0x40E, "display-serial-number", data_type="uint", block=7
            ),
            "display-base-software-version": ParamMask(
                0x410, "display-base-software-version", block=7, mask=0xFF
            ),
            "display-application-version-lua": ParamMask(
                0x411, "display-application-version-lua", block=7, mask=0xFF
            ),
        }
        self.postbox_lock = asyncio.Lock()
        self.parameters["postbox"] = {
            "linearity-test-time": 0b00,
            "t90-test-time": 0b10,
            "telemetry-test-time": 0b01,
            "rtc-time": 0b11,
        }
        self.parameter_handlers["postbox"] = self.parameter_postbox_reader
        events.subscribe(
            self.update_analog_units,
            topic=f"parameter_trigger/{self.current_state['dev-id']}/data-analog",
            parent=self,
        )
        events.subscribe(
            self.update_detector,
            topic=f"parameter_trigger/{self.current_state['dev-id']}/detector-data-invalid",
            parent=self,
        )
        events.subscribe(
            self.update_detector_type,
            topic=f"parameter_trigger/{self.current_state['dev-id']}/detector-type-raw",
            parent=self,
        )
        events.subscribe(
            self.update_bypass_references,
            topic=f"parameter_trigger/{self.current_state['dev-id']}/address-flags",
            parent=self,
        )
        events.subscribe(
            self.update_cal_cup_timestamp,
            topic=f"parameter_trigger/{self.current_state['dev-id']}/cal-cup-on",
            parent=self,
        )

    def schedule_reads(self):
        self.controller.schedule_reads.update(
            self._format_schedule_reads(self.triggers["collect"].get("block", []))
        )
        self.controller.schedule_reads.update(
            self._format_schedule_reads(self.triggers["collect"].get("postbox", []))
        )

    def update_from_roll_call(
        self, serial_number, generation_id, imac_address, version, module_type, **kwargs
    ):
        # TODO version is broken into sensor type
        # TODO make sure we get aim compatibility mode and senor type
        new_params = {
            "serial_number": serial_number,
            "generation_id": generation_id,
            f"address-{self.types[module_type]}": imac_address,
            f"module_type-{self.types[module_type]}": module_type,
            "detector-type-raw": version,
            "dev-id": f"{serial_number}-G{generation_id + 1}",
        }
        if module_type in [61, 62]:
            new_params.pop("detector-type-raw")
        if self.types[module_type] == "flags":
            new_params["address"] = imac_address
        events.publish(
            "imac_module_data",
            data={new_params["dev-id"]: new_params},
            timestamp=datetime.utcnow(),
        )
        self.current_state.update(new_params)
        for trig in self.triggers.get("collect", {}).get("read", []):
            trig.device = self.current_state["dev-id"]
        self.update_specs()

    async def update_detector(self, data, timestamp) -> None:
        """
        Called when the detector type could have changed due to change in head or corrupt image
        :param data:
        :param timestamp:
        :return:
        """
        if data:
            log.info(
                f"Hardware fault for {self.current_state['dev-id']}, resetting detector type to unknown"
            )
            await self.update_detector_type(0, timestamp)
        elif self.current_state["detector-type"] == 0:
            log.info(
                f"Detector {self.current_state['dev-id']} is now healthy. Reading detector type"
            )
            self.reset_deadline_state(
                {"detector-type-raw", "set-point-1", "set-point-2", "set-point-3"}
            )

    async def update_detector_type(self, data, timestamp) -> None:
        """
        Called when the detector type needs updating due to a new detector-type-raw reading
        """
        if self.current_state.get("detector-data-invalid"):
            self.current_state["detector-type"] = 0
            events.publish(
                "imac_module_data",
                data={self.current_state["dev-id"]: {"detector-type": 0}},
                timestamp=timestamp,
            )
        else:
            self.current_state["detector-type"] = data
            events.publish(
                "imac_module_data",
                data={self.current_state["dev-id"]: {"detector-type": data}},
                timestamp=timestamp,
            )

    def update_specs(self):
        for mod_type in self.types.values():
            address = self.current_state.get(f"address-{mod_type}")
            if address:
                address = int(address)
                if mod_type == "flags":
                    # Gets all individual data-flags parameters
                    # NOTE: This does not return the overall register
                    self.parameters["poll"][f"data-{mod_type}"] = ParamBits(
                        address,
                        {
                            # "di4-bypass": 15, -> This is set in update_bypass_references
                            "telemetry-test": 14,
                            "hardware-fault": 13,
                            "ch4-over-range-ndir-incomplete-calibration": 12,
                            "linearity-test-overdue": 11,
                            "detector-warm-up-busy": 10,
                            "gas-value-invalid": 9,
                            "cal-cup-on": 8,
                            "detector-data-invalid": 7,
                            "power-alarm-trip": 6,
                            "power-alarm-warn": 5,
                            "set-point-2-not-3": 4,
                            "set-point-not-1-not-2": 3,
                            "set-point-alarm-3": 2,
                            "set-point-alarm-2": 1,
                            "set-point-alarm-1": 0,
                        },
                    )
                    # Sets the overall data-flags register as a parameter
                    self.parameters["poll"][f"data-{mod_type}-raw"] = Param(
                        address, f"data-{mod_type}"
                    )
                    self.parameters["poll"][f"trip-status"] = ParamMaskBool(
                        address, "trip-status", 0b0011111011000101
                    )
                else:
                    self.parameters["poll"][f"data-{mod_type}"] = Param(
                        address, f"data-{mod_type}"
                    )

                self.parameters["poll"][f"status-{mod_type}"] = ParamBits(
                    address + 0x100,
                    bitmask={
                        f"status-{mod_type}-on-scan-bit": 0,
                        f"status-{mod_type}-l1-clash-bit": 1,
                        f"status-{mod_type}-global-bit": 2,
                        f"status-{mod_type}-l1-own-bit": 3,
                        f"status-{mod_type}-l2-own-bit": 4,
                        f"status-{mod_type}-sys-own-bit": 5,
                        f"status-{mod_type}-l2-clash-bit": 6,
                        f"status-{mod_type}-high-byte-bit": 7,
                        f"status-{mod_type}-valid-offline": 8,
                        f"status-{mod_type}-valid-online": 9,
                        f"status-{mod_type}-valid-iso-request": 10,
                        f"status-{mod_type}-iso-req-filter": 12,
                        f"status-{mod_type}-iso-here": 13,
                        f"status-{mod_type}-iso-there": 14,
                        f"status-{mod_type}-iso-neither": 15,
                    },
                )
                self.parameters["poll"][f"resistance-{mod_type}"] = Param(
                    address + 0x200, f"status-{mod_type}"
                )
                self.parameters["poll"][f"error-offline-count-{mod_type}"] = ParamMask(
                    address + 0x300, f"error-offline-count-{mod_type}", mask=0xFF
                )
                self.parameters["poll"][f"error-clashes-count-{mod_type}"] = ParamMask(
                    address + 0x300,
                    f"error-clashes-count-{mod_type}",
                    mask=0xFF00,
                    rshift=8,
                )
            else:
                # If there is no address, then there is no module data to compute
                self.parameters["poll"].pop(f"data-{mod_type}", None)
                self.parameters["poll"].pop(f"status-{mod_type}", None)
                self.parameters["poll"].pop(f"resistance-{mod_type}", None)
                self.parameters["poll"].pop(f"error-offline-count-{mod_type}", None)
                self.parameters["poll"].pop(f"error-clashes-count-{mod_type}", None)

            if self.current_state.get("aim-compatibility-mode"):
                self.parameters["block"]["power-point-alarm"] = ParamMaskScale(
                    0x40F,
                    "power-point-alarm",
                    block=2,
                    scale=0.01,
                    significant_figures=4,
                )
                self.parameters["block"]["power-point-trip"] = ParamMaskScale(
                    0x410,
                    "power-point-trip",
                    block=2,
                    scale=0.01,
                    significant_figures=4,
                )
            else:
                self.parameters["block"]["power-point-alarm"] = ParamMaskScale(
                    0x410,
                    "power-point-alarm",
                    mask=0xFF00,
                    rshift=8,
                    block=2,
                    scale=0.1,
                    significant_figures=3,
                )
                self.parameters["block"]["power-point-trip"] = ParamMaskScale(
                    0x410,
                    "power-point-trip",
                    mask=0xFF,
                    block=2,
                    scale=0.1,
                    significant_figures=3,
                )

    def __repr__(self):
        return (
            f"{self.name} <Serial {self.current_state.get('serial_number')}"
            f"-G{self.current_state.get('generation_id', -2) + 1}: "
            f"flags @ {self.current_state.get('address-flags', 'unknown')} "
            f"analog @ {self.current_state.get('address-analog', 'unknown')} "
            f"power @ {self.current_state.get('address-power', 'unknown')}>"
            f"bypass @ {self.current_state.get('address-bypass', 'unknown')}>"
        )

    async def parameter_postbox_reader(self, data: set):
        postboxes = {
            postbox: code
            for postbox, code in self.parameters["postbox"].items()
            if postbox in data
        }
        parameters = {}
        for postbox, code in postboxes.items():
            async with self.postbox_lock:
                try:
                    await self.write_parameters({"postbox-selection": code})
                    await asyncio.sleep(2)
                    data = await self.read_parameters({"postbox-timestamp"})
                    parameters.update(data)
                    parameters[postbox] = data["postbox-timestamp"]
                except (ValueError, IOError):
                    log.error(
                        f"Failed to read {self.current_state['dev-id']}: {postbox}"
                    )
        return parameters

    def update_analog_units(self, data, timestamp):
        try:
            converted = self.analog_conversion[
                self.current_state["detector-type"]
            ].decode(data)
        except KeyError:
            return
        self.update_current_state(converted)
        events.publish(
            "imac_module_data",
            data={self.current_state["dev-id"]: converted},
            timestamp=timestamp,
        )

    async def update_bypass_references(self, data, timestamp):
        """
        Determines the bypass references based on the flags register of the detector.
        By-passable flags addresses are address 1-40.
        Local bypass is address-flags + 80 where a DI4 lower byte will have the local bypass status as an input.
        Remote bypass is the modbus addresses in the imac controller for controlling the remote bypass of individual
        detectors. These are defined in addresses 0x527 - 0x529.
        NOTE: this behaviour could change on different SLP code implementations.
        This is based on pyaware/controllers/imac2/ensham_schema.yaml for address layout
        :param data: The new address-flags
        :param timestamp:
        :return:
        """
        try:
            external_params = self.parameters["external"]
        except KeyError:
            self.parameters["external"] = {}
            external_params = self.parameters["external"]

        if 1 <= data <= 40:
            external_params["bypass-remote"] = ParamMask(
                0x527 + ((data - 1) // 16),
                "bypass-remote",
                1 << ((data - 1) % 16),
                rshift=((data - 1) % 16),
            )
            external_params["bypass-local"] = ParamMask(data + 80, "bypass-local", 0b1)

    async def update_cal_cup_timestamp(self, data, timestamp):
        """
        If the cal-cup is removed, we want to read back the calibration timestamp from the gasguard
        :param data:
        :param timestamp:
        :return:
        """
        if not data:
            if "cal-cup-on" in self.send_state:
                log.info(
                    f"Cal cup removed from {self.current_state['dev-id']}. Reading calibration data"
                )

                async def read_cal_cup():
                    await asyncio.sleep(20)
                    self.reset_deadline_state(
                        {
                            "linearity-test-last-points",
                            "linearity-test-alarm-14-days",
                            "cal-cup-alarm-28-days",
                            "linearity-test-time",  # Postbox
                            "t90-test-time",  # Postbox
                        }
                    )

                asyncio.create_task(read_cal_cup())


module_types = {
    # 0: "Reserved",
    # 1: "Controller",
    # 2: "TCD2 DIPSwitch",
    # 3: "EOL Module",
    # 4: "SQM Module",
    # 5: "DI2/4 Module",
    # 6: "IIM-OLC Module",
    7: Lim,
    # 8: "TCD4 Long",
    # 9: "TCD4 Module",
    # 10: "RTD3 Flags",
    # 11: "RTD3 Temp 1",
    # 12: "RTD3 Temp 2",
    # 13: "RTD3 Temp 3",
    # 14: "DI4L Module",
    15: Di4,
    # 16: "IIM Module",
    # 17: "PGM-A Programr",
    # 18: "MEOL Module",
    # 19: "Undefined",
    # 20: "SSW Flags",
    # 21: "SSW Control",
    # 22: "SSW % Slip",
    # 23: "SSW % Speed",
    # 24: "SSW Linr Speed",
    25: Pim,
    26: Do44,
    # 27: "GAI3 Flags",
    # 28: "GAI3 Analogue #1",
    # 29: "GAI3 Analogue #2",
    # 30: "GAI3 Analogue #3",
    # 31: "RKM Keypad",
    # 32: "LED4 Module",
    # 33: "EMM Module",
    # 34: "Undefined #34",
    35: SimP,
    36: SimT,
    37: SimG,
    # 38: "DI5 Module",
    39: Ro4,
    40: Do4,
    # 41: "GCA Flags",
    # 42: "GCA 15Min Tally",
    # 43: "GCA 8Hr Tally",
    # 44: "GCA 24Hr Tally",
    # 45: "GCA Raw Count",
    # 46: "DI8 Module",
    # 47: "RIS Module",
    48: Aim,  # AIM Flags
    49: Aim,  # AIM Analog
    50: Aim,  # AIM PwrSupply
    # 51: "CRM Module",
    # 52: "ARM Module",
    # 53: "GRM Module",
    54: Rtd1,
    55: Rtd1,
    # 56: "SIM-G2 Module",
    # 57: "FCP DigInputs",
    # 58: "FCP DigOutputs",
    # 59: "FCP AnaInputs",
    # 60: "FCP AnaOutputs",
    61: GasGuard2,  # Gasguard2Flags,
    62: GasGuard2,  # Gasguard2Analog,
    63: GasGuard2,  # Gasguard2PowerSupply,
    "rts": RtsModule,
}
