import pyscreenshot as ImageGrab
import pytesseract
import time
import pydirectinput
import random
import glob
import os
from datetime import datetime
from win32api import GetSystemMetrics
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
options = webdriver.ChromeOptions() 
options.add_argument('--headless') 
options.page_load_strategy = 'none' 
chrome_path = ChromeDriverManager().install() 
chrome_service = Service(chrome_path) 
driver = Chrome(options=options, service=chrome_service) 
driver.implicitly_wait(5)

#config
waitFirst = True
waitEver = True
secondsToEnd = 999999999
logPath = 'C:/FF11/HorizonXI/Game/chatlogs/*'
goleft = 'a'
goright = 'd'
failCount = 0
shouldWaitCount = 0
screenWidth = GetSystemMetrics(0)
screenHeight = GetSystemMetrics(1)
fishToCatch= 'eel'
timeurl = "http://www.pyogenes.com/ffxi/timer/v2.html"
driver.get(timeurl) 
time.sleep(5)
content = driver.find_element(By.ID, "vTime")

begin = time.time()

while(True):
    if datetime.now().hour == 24 and (datetime.now().minute == 58 or datetime.now().minute == 59):
        time.sleep(120)
    list_of_files = glob.glob(logPath)
    searching = True
    fish = True
    logout=False
    wait=False
    lasttime = time.time()

    latest_file = max(list_of_files, key=os.path.getctime)
    logfile = open(latest_file)
    logfile.seek(0,2) # Go to the end of the file

    if waitFirst == True:
        waitFirst = False
        wait = True
        searching = False
        fish = False
    else:
        pydirectinput.press('/')
        pydirectinput.press('f')
        pydirectinput.press('i')
        pydirectinput.press('s')
        pydirectinput.press('h')
        pydirectinput.press('enter')
        lasttime = time.time()

    while(searching):
        line = logfile.readline()
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        print(line)
        laptime = round((time.time() - lasttime), 2)
        if(laptime > 25):
            searching = False
            fish = False
            pydirectinput.press('esc')
            time.sleep(random.randint(4,6))
        if "Something caught the hook!!!" in line or "You feel something pulling at your line." in line or "Something clamps onto your line ferociously!" in line or "You didn't catch anything." in line:
            fish = False
            searching = False
            failCount = 0
            shouldWaitCount = 0
            time.sleep(1)
            pydirectinput.press('esc')
            time.sleep(random.randint(5,6))
        elif "Something caught the hook!" in line:
            line = logfile.readline()
            print(line)
            while not line:
                line = logfile.readline()
                print(line)

            if ("You have a good feeling about this one!" in line or "Your keen angler's senses tell you that this is the pull of" in line) and "crayfish" not in line :
                fish = True
                searching = False
                failCount = 0
                shouldWaitCount = 0
            else:
                fish = False
                searching = False
                failCount = 0
                shouldWaitCount = 0
                time.sleep(1)
                pydirectinput.press('esc')
                time.sleep(random.randint(5,6))
        if "fish without bait" in line or "Nohrin regretfully" in line or "cannot fish here" in line:
            failCount = failCount + 1
            searching = False
            logout=True
            shouldWaitCount = 0
            if "Nohrin regretfully" in line:
                failCount = failCount + 99
        if "pulling at" in line or "You didn't catch anything." in line:
            shouldWaitCount = shouldWaitCount + 1
            if shouldWaitCount > 4:
                searching = False
                wait = True
                shouldWaitCount = 0

    totaltime = round((time.time() - begin), 2)

    if(logout == True or totaltime > secondsToEnd):
        if failCount < 3:
            pydirectinput.press('/')
            pydirectinput.press('e')
            pydirectinput.press('q')
            pydirectinput.press('u')
            pydirectinput.press('i')
            pydirectinput.press('p')
            pydirectinput.press('s')
            pydirectinput.press('e')
            pydirectinput.press('t')
            pydirectinput.press('space')
            pydirectinput.press('1')
            pydirectinput.press('enter')
            logout = False
        else:
            pydirectinput.press('/')
            pydirectinput.press('l')
            pydirectinput.press('o')
            pydirectinput.press('g')
            pydirectinput.press('o')
            pydirectinput.press('u')
            pydirectinput.press('t')
            pydirectinput.press('enter')
            break

    lasttime = time.time()
    while(fish):
        X1 = int(screenWidth * .078125)
        Y1 = int(screenHeight * .20833)
        X2 = int(screenWidth * .9375)
        Y2 = int(screenHeight * .55555)
        im = ImageGrab.grab(bbox=(X1, Y1, X2, Y2)) 
        pix = im.load()

        rl,gl,bl = pix[int((X2 - X1) * .16545),int((Y2 - Y1) * .56)]
        rr,gr,br = pix[int((X2 - X1) * .81818),int((Y2 - Y1) * .56)]
        rm,gm,bm = pix[int((X2 - X1) * .45863),int((Y2 - Y1) * .024)]
        # print(rl)
        # print(gl)
        # print(bl)
        # print(rr)
        # print(gr)
        # print(br)
        # print(rm)
        # print(gm)
        # print(bm)
        # print('ok')
        if(rl > 105 or bl > 105 or gl > 105):
            print('L')
            lasttime = time.time()
            pydirectinput.press(goleft)
            time.sleep(.2)
        if(rr > 105 or br > 105 or gr > 105):
            print('R')
            lasttime = time.time()
            pydirectinput.press(goright)
            time.sleep(.2)
        
        if rm < 200:
            pydirectinput.press('enter')
            fish = False
            time.sleep(random.randint(5,6))

    lasttime = time.time()

    line = logfile.readline()
    print(line)
    while line:
        line = logfile.readline()
        print(line)
        if fishToCatch in line:
            wait = False

    prevHour = int(content.text[len(content.text) - 8:len(content.text) - 6])

    while(wait and waitEver):

        hourDigit = int(content.text[len(content.text) - 8:len(content.text) - 6])

        if hourDigit != prevHour:
            if hourDigit == 0 or hourDigit == 4 or hourDigit == 6 or hourDigit == 7 or hourDigit == 17 or hourDigit == 18 or hourDigit == 20:
                wait = False
        prevHour = hourDigit
        
        lasttime = time.time()

        line = logfile.readline()
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        print(line)

        if fishToCatch in line:
            wait = False
