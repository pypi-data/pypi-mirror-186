# Local MQTT Example Configuration
## Folder Structure
A generic folder structure is shown below that details the path each config file should be found in. Starting at the 
AWAREPATH i.e. /etc/AWARE (on Linux).
```console
.
└── config
    ├── connection.yaml
    ├── gateway.yaml
    └── translation.yaml
```
### Config
The "config" folder contains "connection.yaml", "gateway.yaml" (device and pyaware configuration) and "translation.yaml" (server and device configuration). 

"connection.yaml" in this example contains,
* The disable feature flag for MQTT as it is not required in most solar qube applications.

"gateway.yaml" in this example contains,
* The configuration for two modbus devices and an SP PRO serial device.
* Path linking to these devices.

"translation.yaml" in this example contains,
* The modbus server mapping for the above devices to read/write to the server.
  
For more information about how to construct these config files, please see the main README.md file.