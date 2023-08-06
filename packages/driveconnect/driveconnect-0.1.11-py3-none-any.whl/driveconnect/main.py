import ctypes
import platform
import string
import pprint
import subprocess


# initialize pprint
pp = pprint.PrettyPrinter(width=41)

def set_pprint_width(width):
    '''
    Reset pretty printer width value
    '''
    global pp
    pp._width = width


# for logging

def log_it(log, level, message, _print=False):
    '''
    Log the `message` at the given `level` (as string) when a logger is given.
    '''
    if log:
        _level = level.lower()
        assert _level in ("notset", "debug", "info", "warning", "error", "critical")
        getattr(log, _level)(message)
    if _print:
        if log:
            pp.pprint("## logged the message:")
        else:
            pp.pprint("## didn't log the message:")
        pp.pprint(message)
        

        
# command execution

def cmd(cmd, log=None, level="info", _print=False):
    '''
    Run a command in cmd.exe and return its value.
    '''
    try:
        res = subprocess.call(cmd, shell=True)
        log_it(log, level, f"Successfully executed `{cmd}`.", _print=_print)
    except Exception as e:
        log_it(log, level, f"Failed to execute `{cmd}`:\n{e}.", _print=_print)
        
def compress(data, selectors):
    '''
    Filter data by selectors.
    '''
    for d, s in zip(data, selectors):
        if s:
            yield d

def get_available_drives():
    '''
    Which drives are available on this Windows computer?
    '''
    # nice solution from: https://stackoverflow.com/questions/4188326/in-python-how-do-i-check-if-a-drive-exists-w-o-throwing-an-error-for-removable
    if 'Windows' not in platform.system():
        return []
    drive_bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
    return list(compress(string.ascii_uppercase,
                         map(lambda x: ord(x) - ord('0'),
                             bin(drive_bitmask)[:1:-1])))

def is_drive_connected(drive_letter):
    '''
    Is the drive currently connected? `drive_letter` with or without `:`.
    '''
    drive_letter = drive_letter.rstrip(':')
    return drive_letter in get_available_drives()

# https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)
# https://discuss.dizzycoding.com/what-is-the-best-way-to-map-windows-drives-using-python/
# the first possibility

def _connect_drive(drive_letter, server_path, username, password, log=None, level="info", _print=False):
    '''
    Command to connect the drive (`net user` in cmd.exe).
    '''
    drive_letter = drive_letter.rstrip(':')
    server_path = server_path.lstrip('\\')
    cmd_ = f"net use {drive_letter}: \\\\{server_path} /user:{username} {password}"
    return cmd(cmd_, log=log, level=level, _print=_print)

def _disconnect_drive(drive_letter, log=None, level="info", _print=False):
    '''
    Disconnect the drive (`net use` in cmd.exe).
    '''
    drive_letter = drive_letter.rstrip(':')
    cmd_ = f"net use {drive_letter}: /del /y"  # the /y is silently set prompt to `Yes`
    return cmd(cmd_, log=log, level=level, _print=_print)

def _assess_connection(drive_letter, server_path=None, log=None, level="info", _print=False):
    if is_drive_connected(drive_letter):
        log_it(log, level, f"`{'Server' if server_path is None else server_path}` is connected via `{drive_letter}:`", _print=_print)
    else:
        log_it(log, level, f"`{'Server' if server_path is None else server_path}` is not connected via `{drive_letter}`.", _print=_print)

def connect_drive(drive_letter, server_path, username=None, password=None, co=None, log=None, level="info", _print=False, reconnect=False):
    '''
    Connect the drive to a server handling the credentials.
    Either give username and password directly or take a credential object from the package `pycryptaes`.
    '''
    drive_letter = drive_letter.rstrip(':')
    if is_drive_connected(drive_letter) and reconnect:
        log_it(log, level, f"Drive `{drive_letter}:` is already connected. Reconnecting the drive.", _print=_print)
        _disconnect_drive(drive_letter, log=log, level=level, _print=_print)
        log_it(log, level, f"Attempting to reconnect `{drive_letter}:` to `{server_path}`.", _print=_print)
        connect_drive(drive_letter, server_path, username, password, co=co, log=log, level=level, _print=_print)
    elif username is None and password is None and co is None:                  # in this case, interactively input password
        server_path = server_path.lstrip('\\')                                  # ensuring correct `\\\\` in front of server path
        cmd_ = f"net use {drive_letter}: \\\\{server_path}"
        cmd(cmd_, log=log, level=level, _print=_print)
    elif co is not None:
        _connect_drive(drive_letter, server_path, co.username, co.password, log=log, level=level, _print=_print)
    elif username is not None and password is not None:
        _connect_drive(drive_letter, server_path, username, password, log=log, level=level, _print=_print)
    # when exciting, display the current state:
    _assess_connection(drive_letter=drive_letter, server_path=server_path, log=log, level=level, _print=_print)
        
def disconnect_drive(drive_letter, log=None, level="info", _print=False):
    drive_letter = drive_letter.rstrip(':')
    if is_drive_connected(drive_letter):
        _disconnect_drive(drive_letter, log=log, level=level, _print=_print)
    else:
        log_it(log, level, f"`{drive_letter}:` is already disconnected.", _print=_print)
    # when exciting, display the current state:
    _assess_connection(drive_letter=drive_letter, log=log, level=level, _print=_print)
