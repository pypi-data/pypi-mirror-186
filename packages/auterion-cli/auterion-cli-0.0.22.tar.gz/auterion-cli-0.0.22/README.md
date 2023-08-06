# Auterion CLI

Command line utility to interact with Auterion Devices and Apps

## Installation

Use pip

```
pip3 install auterion-cli
```

This will install in your local user directory. Make sure your `.local/bin` directory is in your path to access it. Not recommended, but you can also install it globally on your system.


## Usage

You can type `auterion-cli` in your command line to get an overview of available commands.

### Discover / select devices

"Selecting" a device makes auterion-cli perform all actions against that selected device. 
In case no device is selected, auterion-cli will default to any device reachable on `10.41.1.1`

- `auterion-cli device discover`: Discover reachable auterion devices
- `auterion-cli device select <serial>`: Select a reachable device to connect to
- `auterion-cli device deselect`: De-select any currently selected device

### Device information

- `auterion-cli info`: Get information about the selected device
- `auterion-cli report`: Download diagnostic report from selected device

### App management

- `auterion-cli app list`: List all currently installed apps on the device
- `auterion-cli app start <app name>`: Start a stopped app
- `auterion-cli app stop <app name>`: Stop a running app
- `auterion-cli app restart <app name>`: Restart an app
- `auterion-cli app enable <app name>`: Enable autostart for an app
- `auterion-cli app disable <app name>`: Disable autostart for an app
- `auterion-cli app status <app name>`: Get current status for an app
- `auterion-cli app logs <app name> [-f]`: Display logs for an app. `-f` for live log feed

### Development workflow

- `auterion-cli app init`: Create a new app project
- `auterion-cli app build`: Build the app project in current folder. Creates *.auterionos* file in build folder.
- `auterion-cli app install <file>`: Install the *.auterionos* app file to skynode

