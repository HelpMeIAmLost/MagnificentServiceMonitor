# Magnificent Service Monitor
## Description
Checks on the Magnificent service every once in a while, as indicated by the ```interval``` parameter. If the Magnificent has been unresponsive for 5 minutes, a notification will pop-up. This is aside from the output log file ```server.log``` being updated by this application.

## Requirements
* Linux or macOS systems only

## Usage
### Command line syntax
```
python service_monitor.py service server [interval]
```
* ```service``` - TCP or HTTP
* ```server``` - server address and port number (e.g. ```localhost:12345```)
* ```interval``` - *Optional* check interval in seconds (default is set to 10)

Runs and checks on the Magnificent service
