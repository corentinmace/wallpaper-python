import os
import sys
import glob
import time
import random
from PIL import Image
import win32api, win32con, win32gui
from datetime import *

HOUR = datetime.now().hour

os.chdir("C:\\wallpaper-python\\wallpapers\\")

def mergeIMG():
	HOUR = datetime.now().hour
	img1 = "C:\\wallpaper-python\\wallpapers\\0\\" + str(HOUR) + ".png"
	img2 = "C:\\wallpaper-python\\wallpapers\\1\\" + str(HOUR) + ".png"
	img3 = "C:\\wallpaper-python\\wallpapers\\2\\" + str(HOUR) + ".png"
	# images = [Image.open(x) for x in [img1, img2, img3]]
	images = [Image.open(x) for x in [img1, img2]]

	widths, heights = zip(*(i.size for i in images))

	# total_width = 4920
	total_width = 3840
	max_height = 1920

	new_im = Image.new('RGB', (total_width, max_height))

	# new_im.paste(images[0], (0, 550))
	# new_im.paste(images[1], (1920, 550))
	# new_im.paste(images[2], (3840, 0))

	new_im.paste(images[0], (0, 0))
	new_im.paste(images[1], (1920, 0))

	new_im.save('final.jpg', quality=100, subsampling=0)
	setWallpaper("C:\\wallpaper-python\\wallpapers\\final.jpg")

# Function to actually set the wallpaper as tiled image
# > We will set background as a single image (which is 2 images merged)
def setWallpaper(path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "1")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)
# ================================================================ #


mergeIMG()