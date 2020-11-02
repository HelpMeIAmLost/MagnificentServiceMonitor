# Magnificent Service Monitor
## Description
Checks on the Magnificent service every once in a while, as indicated by the ```interval``` parameter. If the Magnificent has been unresponsive for 5 minutes, a notification will pop-up.

## Requirements
* Linux or macOS systems only

## Usage
### Command line syntax
```
python service_monitor.py service server [interval]
```
* ```service``` - TCP or HTTP
* ```server``` - server address and port number (e.g. ```localhost:12345```)
* ```interval``` - *Optional* Check interval in seconds

Runs and checks on the Magnificent service
