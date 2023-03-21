import pyscreenshot as ImageGrab
import cv2
import pytesseract
from PIL import Image
import time
from skimage import util
import pydirectinput
import random
import glob
import os
import re


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#functions
def follow(thefile):
    thefile.seek(0,2) # Go to the end of the file
    while True:
        try:
            line = thefile.readline()
            if not line:
                time.sleep(0.1) # Sleep briefly
                continue
            yield line
        except:
           print('error')

#config
waitFirst = False
secondsToEnd = 999999999
logPath = 'C:/FF11/HorizonXI/Game/chatlogs/*'
list_of_files = glob.glob(logPath)
latest_file = max(list_of_files, key=os.path.getctime)
goleft = 'a'
goright = 'd'
failCount = 0
shouldWaitCount = 0

logfile = open(latest_file)
loglines = follow(logfile)
for line in loglines:
 print(line, end='')
 if ("{Teleport-Dem}" in line or "{Teleport-Holla}" in line or "{Teleport-Mea}" in line) and '{Can I have it?}' in line and 'Jeuno' in line :
    inilist = [i.start() for i in re.finditer('[', line)]
    name = line[line.index(']')+2:inilist[1]]
    pydirectinput.press('/')
    pydirectinput.press('p')
    pydirectinput.press('c')
    pydirectinput.press('m')
    pydirectinput.press('d')
    pydirectinput.press('space')
    pydirectinput.press('a')
    pydirectinput.press('d')
    pydirectinput.press('d')
    for char in name:
        pydirectinput.press(char)
    pydirectinput.press('enter')


