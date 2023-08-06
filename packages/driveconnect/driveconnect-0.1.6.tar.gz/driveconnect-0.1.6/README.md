# Installation

```
pip install driveconnect
```
Or:
```
pip install git+https:\\github.com\gwangjinkim\driveconnect.git
```

# Usage

```
import driveconnect as dcn

# test, wether a drive e.g. 'M:' is connected:
dcn.is_drive_connected(drive_letter='M') # it works also with "M:"
## False

# set the credentials for the server in local folders
dcn.pss.set_credentials('.\.user', '.\.pass')

# connect to the server
# leading '\\' can be left out in server address and the 'M:' as well as 'M' both work
dcn.connect_drive('M:', '\\serveraddress\folder', '.\.user', '.\.pass')

# disconnect from the server
dcn.disconnect_drive('M:')
```
