import struct
import ctypes
from datetime import *

HOUR = datetime.now().hour

SPI_SETDESKWALLPAPER = 20

def is_64_windows():
    return struct.calcsize('P') * 8 == 64

def get_sys_parameters_info():
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def set_wallpaper(path):
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, path, 3)

    if not r:
        print(ctypes.WinError())

def change_wallpaper(wallpaper_number):
    print("here", wallpaper_number)
    WALLPAPER_PATH = "C:\\" + str(wallpaper_number) + ".jpg"

    set_wallpaper(WALLPAPER_PATH)

change_wallpaper(HOUR)

