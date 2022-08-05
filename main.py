import os
import sys
import glob
import time
import random
from PIL import Image
import win32api, win32con, win32gui
from datetime import *
from screeninfo import get_monitors, Monitor

HOUR = datetime.now().hour

os.chdir("C:\\wallpaper-python\\wallpapers\\")

def mergeIMG():
	
	total_width = 0
	max_height = 0
	monitors= get_monitors()
	imagesArray = []

	for m in monitors:
		total_width += m.width
		if m.height != max_height - m.y or m.height > max_height + m.y:
			y = abs(m.y)
			max_height = m.height + y

	for i in range(len(monitors)):
		img = "C:\\wallpaper-python\\wallpapers\\" + str(i) + "\\" + str(HOUR) + ".png"
		imagesArray.append(img)
		i += 1

	images = [Image.open(x) for x in imagesArray]
	widths, heights = zip(*(i.size for i in images))


	new_im = Image.new('RGB', (total_width, max_height))

	position_x = 0
	position_y = 0
	for i in range(len(images)):
		if monitors[i].y < 0:
			position_y = 0 - monitors[i].y
		else: 
			position_y = 0 + monitors[i].y
		new_im.paste(images[i], (position_x, position_y))
		position_x = widths[i]
		i += 1


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
