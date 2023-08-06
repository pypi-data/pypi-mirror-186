# Installation

```
pip install driveconnect
```
Or:
```
pip install git+https:\\github.com\gwangjinkim\driveconnect.git
```
Or:
```
pipenv install git+https:\\github.com\gwangjinkim\driveconnect.git#egg=driveconnect
```
Or:
```
poetry add driveconnect  # version number: driveconnect==0.1.8
```
Or (from github repo):
```
poetry add git+ssh://git@github.com/gwangjinkim/driveconnect.git#main
```

# Usage

```
import driveconnect as dcn
import pycryptaes as pca
import logging as log

print(dcn.__version__)

# set better pretty print for log message on stdout:
dcn.set_pprint_width(width=81)

# instanciate encryptor
ca = pca.AES()
# for saving some typing on REPL:
home = "C:/Users/myusername"
p = lambda x: f"{home}/{x}"
args = (p(".key"), p(".user"), p(".pass"))

# set logger
log.basicConfig(filename=f"{home}/mylog.log", filemode='a', level=log.DEBUG)


# if first time using credentials, you have to enter username and password after typing:
ca.generate_key_user_pass(*args)

# otherwise comment out the previous line and collect/read the previously saved credentials:
co = ca.read_key_user_pass(*args)           # `co` = `Credential Object`

# now you can test, wether a drive e.g. 'G:' is connected:
dcn.is_drive_connected(drive_letter='G') # it works also with "G:"
## False

# connect to the server
# leading '\\' can be left out in server address and the 'M:' as well as 'M' both work
dcn.connect_drive('G:', '\\serveraddress\folder', co=co, log=log, level="info")
# or for connections where no credentials are needed:
dcn.connect_drive('G:', '\\serveraddress\folder', log=log, level="info", _print=True)
# `log=`, `level=` and `_print=` are optional.

# disconnect from the server
dcn.disconnect_drive('G:', log=log, level="info", _print=True)
# or without logger:
dcn.disconnect_drive('G:', _print=True)
```
