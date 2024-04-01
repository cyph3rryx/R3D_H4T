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
            _winreg.SetValueEx(key, "DisableAntiSpyware", 0, _winreg.REG_DWORD, 1)
            new_key = _winreg.CreateKey(key, "Real-Time Protection")
            _winreg.SetValueEx(new_key, "DisableRealtimeMonitoring", 0, _winreg.REG_DWORD, 1)
            _winreg.SetValueEx(new_key, "DisableBehaviorMonitoring", 0, _winreg.REG_DWORD, 1)
            _winreg.SetValueEx(new_key, "DisableScanOnRealtimeEnable", 0, _winreg.REG_DWORD, 1)
            _winreg.SetValueEx(new_key, "DisableOnAccessProtection", 0, _winreg.REG_DWORD, 1)
            _winreg.SetValueEx(new_key, "DisableIOAVProtection", 0, _winreg.REG_DWORD, 1)
            _winreg.CloseKey(key)
            _winreg.CloseKey(new_key)
            print("Windows Defender has been disabled.")
            print("Please restart your computer to take effect.")
            getchar()
            return 0
        else:
            print("Could not open the key. Make sure you have the correct permissions.")
            return
    else:
        print("Please run this script as an administrator.")
        return -1

if __name__ == '__main__':
    result = modify_defender_settings()
    sys.exit(result)
