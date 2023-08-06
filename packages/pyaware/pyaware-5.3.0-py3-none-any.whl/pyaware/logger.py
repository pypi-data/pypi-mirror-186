import logging.handlers
import os
import typing
import types
import sys
from dataclasses import dataclass, field
from functools import wraps
import pyaware.config

log = logging.getLogger(__file__)


def _dict_set_item(prefix: str):
    def dict_set_item(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.debug(f"{prefix}Set item {args}: {kwargs}")
            return func(*args, **kwargs)

        return wrapper

    return dict_set_item


def _dict_update(prefix: str):
    def dict_update(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            input_dict = {}
            input_dict.update(*args, **kwargs)
            current_values = {
                k: self.__getitem__(k)
                for k in input_dict.keys() & self.keys()
                if k in self
            }
            log.debug(
                f"{prefix}Updating current_values {current_values} with {input_dict}"
            )
            return func(*args, **kwargs)

        return wrapper

    return dict_update


@dataclass
class RuntimeLogger:
    debug: typing.Union[bool, dict, list, set] = field(default_factory=dict)
    core: bool = False
    triggers: bool = False
    mqtt: bool = False
    modbus: bool = False
    state_changes: bool = False
    comms: dict = field(default_factory=dict)

    def load(self, debug: typing.Union[dict, list]):
        if type(debug) not in [dict, list]:
            log.warning(f"Invalid debug type set of {debug}")
            return
        self.debug = debug
        self.update()

    def start(self):
        top_log = logging.getLogger()
        logname = os.path.join(pyaware.config.aware_path, "AWARE.log")
        formatter = logging.Formatter(
            "%(asctime)-15s %(threadName)-15s "
            "%(levelname)-8s %(pathname)-15s:%(lineno)-8s %(message)s"
        )
        handler = logging.handlers.TimedRotatingFileHandler(
            logname, when="midnight", backupCount=7
        )
        handler.setFormatter(formatter)
        handler.setLevel(logging.INFO)
        top_log.addHandler(handler)

        screen_handler = logging.StreamHandler(sys.stdout)
        screen_handler.setFormatter(formatter)
        top_log.addHandler(screen_handler)
        screen_handler.setLevel(logging.INFO)

        top_log.setLevel(logging.DEBUG)

    def update(self):
        if "all" in self.debug:
            self.modbus_logging(True)
            self.core_logging(True)
            self.triggers = True
            self.mqtt = True
            self.modbus = True
            self.core = True
            self.state_changes_logging(True)
            return

        elif len(self.debug) == 0:
            self.modbus_logging(False)
            self.core_logging(False)
            self.triggers = False
            self.mqtt = False
            self.modbus = False
            self.core = False
            self.state_changes_logging(False)
            return

        # Set core logging if any logging is enabled
        self.core_logging(True)
        self.core = True

        if "modbus" in self.debug:
            self.modbus = True
            self.modbus_logging(True)
        else:
            self.modbus = False
            self.modbus_logging(False)

        self.triggers = "triggers" in self.debug
        self.state_changes_logging("state_changes" in self.debug)

    @staticmethod
    def modbus_logging(enabled: bool):
        import aiomodbus.serial
        import aiomodbus.tcp

        if enabled:
            for mod in [aiomodbus.serial, aiomodbus.tcp]:
                modbus_log = logging.getLogger(mod.__file__)
                modbus_log.setLevel(logging.DEBUG)
                log_dir = pyaware.config.aware_path / "modbus_log"
                log_dir.mkdir(parents=True, exist_ok=True)
                formatter = logging.Formatter(
                    "%(asctime)-15s %(module)-15s: %(message)s"
                )
                handler = logging.handlers.TimedRotatingFileHandler(
                    log_dir / f"{mod.__name__}.log", "h", backupCount=2
                )
                handler.setFormatter(formatter)
                modbus_log.addHandler(handler)
                modbus_log.propagate = False
        else:
            for mod in [aiomodbus.serial, aiomodbus.tcp]:
                modbus_log = logging.getLogger(mod.__file__)
                modbus_log.handlers.clear()

    def core_logging(self, enabled: bool):
        if enabled:
            for logger in pyaware.log.handlers:
                logger.setLevel(logging.DEBUG)
            return
        else:
            for logger in pyaware.log.handlers:
                logger.setLevel(logging.INFO)
            return

    def register_comms(self, instances: dict):
        self.comms = instances

    def state_changes_logging(self, enabled: bool):
        if enabled:
            for instance in self.comms.values():
                try:
                    objects = instance.get_state_objects()
                    self.wrap_state(objects)
                except AttributeError:
                    continue
        else:
            for instance in self.comms.values():
                try:
                    objects = instance.get_state_objects()
                    self.unwrap_state(objects)
                except AttributeError:
                    continue

    def wrap_state(self, objects: dict):
        for name, obj in objects.items():
            try:
                current = obj.current_state
                self._wrap_dict(f"{name}: Current State: ", current)
            except AttributeError as e:
                pass
            try:
                event = obj.event_state
                self._wrap_dict(f"{name}: Event State: ", event)
            except AttributeError as e:
                pass
            try:
                store = obj.store_state
                self._wrap_dict(f"{name}: Store State: ", store)
            except AttributeError as e:
                pass
            try:
                send = obj.send_state
                self._wrap_dict(f"{name}: Send State: ", send)
            except AttributeError as e:
                pass

    def _wrap_dict(self, msg: str, dictionary: dict):
        dictionary.__setitem__ = types.MethodType(
            _dict_set_item(msg)(dictionary.__setitem__), dictionary
        )
        dictionary.update = types.MethodType(
            _dict_update(msg)(dictionary.update), dictionary
        )

    def unwrap_state(self, objects: dict):
        for name, obj in objects.items():
            try:
                current = obj.current_state
                self._unwrap_dict(current)
            except AttributeError as e:
                pass
            try:
                event = obj.event_state
                self._unwrap_dict(event)
            except AttributeError as e:
                pass
            try:
                store = obj.store_state
                self._unwrap_dict(store)
            except AttributeError as e:
                pass
            try:
                send = obj.send_state
                self._unwrap_dict(send)
            except AttributeError as e:
                pass

    def _unwrap_dict(self, dictionary: dict):
        try:
            dictionary.update = dictionary.update.__wrapped__
        except AttributeError:
            pass
        try:
            dictionary.__setitem__ = dictionary.__setitem__.__wrapped__
        except AttributeError:
            pass


runtime_logger = RuntimeLogger()
