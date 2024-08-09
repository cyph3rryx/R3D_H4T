import _winreg
import os
import sys
import ctypes
from ctypes import wintypes

def is_user_admin():
    user = ctypes.windll.advapi32.GetUserNameW(wintypes.LPWSTR(ctypes.create_unicode_buffer(256))).value.decode('utf-16')
    p = ctypes.windll.shell32.ShellExecuteW(None, None, 'cmd.exe', '/c net localgroup administrators "{}"'.format(user), None, 1)
    if p == 0:
        return False
    else:
        return True

def modify_defender_settings():
    if is_user_admin():
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows Defender', 0, _winreg.KEY_ALL_ACCESS)
        if key:
            
            getchar()
            return 0
        else:
            print("This is a Purple Gate and you have to get the key to open it! Be the freakin' admin to get the key!")
            return
    else:
        print("Human??? Become the admin first then run the code!")
        return -1

if __name__ == '__main__':
    result = modify_defender_settings()
    sys.exit(result)
