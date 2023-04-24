import pyscreenshot as ImageGrab
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

options = webdriver.ChromeOptions() 
options.add_argument('--headless') 
options.page_load_strategy = 'none' 
chrome_path = ChromeDriverManager().install() 
chrome_service = Service(chrome_path) 
driver = Chrome(options=options, service=chrome_service) 
driver.implicitly_wait(5)

#config
waitFirst = False
waitEver = True
hourToEnd = 3
logPath = 'C:/FF11/HorizonXI/Game/chatlogs/*'
goleft = 'a'
goright = 'd'
screenWidth = GetSystemMetrics(0)
screenHeight = GetSystemMetrics(1)
fishToCatch= 'black sole'
timeurl = "http://www.pyogenes.com/ffxi/timer/v2.html"
driver.get(timeurl) 
time.sleep(5)
content = driver.find_element(By.ID, "vTime")
X1 = int(screenWidth * .1)
Y1 = int(screenHeight * .2)
X2 = int(screenWidth * .9)
Y2 = int(screenHeight * .5)
shouldWaitCount = 0
failCount = 0
redY = -1
line = None

#function
def typeout(stringToType):
    for char in stringToType:
        if char == ' ':
            pydirectinput.press('space')
        else:
            pydirectinput.press(char)
    pydirectinput.press('enter')

while(True):
    if datetime.now().hour == 24 and (datetime.now().minute == 58 or datetime.now().minute == 59):
        time.sleep(120)
    list_of_files = glob.glob(logPath)
    searching = True
    fish = True
    logout=False
    wait=False
    lasttime = time.time()
    im = ImageGrab.grab(bbox=(X1, Y1, X2, Y2)) 
    # im.save('test.png')
    pix = im.load()

    rl,gl,bl = pix[int((X2 - X1) * .14),int((Y2 - Y1) * .66)]
    rl2,gl2,bl2 = pix[int((X2 - X1) * .15),int((Y2 - Y1) * .66)]
    rl3,gl3,bl3 = pix[int((X2 - X1) * .16),int((Y2 - Y1) * .66)]
    rr,gr,br = pix[int((X2 - X1) * .86),int((Y2 - Y1) * .66)]
    rr2,gr2,br2 = pix[int((X2 - X1) * .85),int((Y2 - Y1) * .66)]
    rr3,gr3,br3 = pix[int((X2 - X1) * .84),int((Y2 - Y1) * .66)]
    baserl = rl + rl2 + rl3
    basegl = gl + gl2 + gl3
    basebl = bl + bl2 + bl3
    baserr = rr + rr2 + rr3
    basegr = gr + gr2 +gr3
    basebr = br + br2 + br3

    latest_file = max(list_of_files, key=os.path.getctime)
    logfile = open(latest_file)
    logfile.seek(0,2) # Go to the end of the file

    if waitFirst == True:
        waitFirst = False
        wait = True
        searching = False
        fish = False
    else:
        typeout('/fish')

    if searching:
        print('cast')
    while(searching):
        laptime = round((time.time() - lasttime), 2)
        if(laptime > 25):
            searching = False
            fish = False
            pydirectinput.press('esc')
            time.sleep(random.randint(4,6))

        try:
            line = logfile.readline()
        except:
            line = None
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        print(line)
        if fishToCatch in line:
            shouldWaitCount = 0

        if "Something caught the hook!!!" in line or "You feel something pulling at your line." in line or "Something clamps onto your line ferociously!" in line or "You didn't catch anything." in line or "You cannot use that command" in line:
            fish = False
            searching = False
            failCount = 0
            time.sleep(1)
            pydirectinput.press('esc')
            time.sleep(random.randint(5,6))
            shouldWaitCount = shouldWaitCount + 1
            print(shouldWaitCount)
            if shouldWaitCount > 4:
                searching = False
                wait = True
        elif "Something caught the hook!" in line:
            failCount = 0
            try:
                line = logfile.readline()
            except:
                line = None
            print(line)
            while not line:
                try:
                    line = logfile.readline()
                except:
                    line = None
                print(line)

            if ("You have a good feeling about this one!" in line or "Your keen angler's senses tell you that this is the pull of" in line) and "crayfish" not in line :
                fish = True
                searching = False
            else:
                fish = False
                searching = False
                time.sleep(1)
                pydirectinput.press('esc')
                time.sleep(random.randint(5,6))
        elif "fish without bait" in line:
            failCount = failCount + 1
            if failCount < 3:
                print('equipset 1')
                typeout('/equipset 1')
            else:
                logout=True
            searching = False
        elif "Nohrin regretfully" in line or "cannot fish here" in line:
            searching = False
            logout=True
        elif "You cannot use that command while unconscious" in line:
            pydirectinput.press('enter')
            pydirectinput.press('enter')
            pydirectinput.press('enter')
            time.sleep(30)
            failCount = failCount + 1
            if failCount < 3:
                pydirectinput.press('enter')
            else:
                logout=True
            searching = False
            
    if logout:
        print('logout')
    if(logout == True or datetime.now().hour == hourToEnd):
        typeout('/logout')
        break

    if fish:
        print('fish')
        shouldWaitCount = 0
    while(fish):
        im = ImageGrab.grab(bbox=(X1, Y1, X2, Y2)) 
        # im.save('test.png')
        pix = im.load()

        if redY == -1:
            for i in range(1, Y2 - Y1):
                r,g,b = pix[int((X2 - X1) * .465),int(i)]
                if r > 200:
                    print(i)
                    redY = i
                    break

        rl,gl,bl = pix[int((X2 - X1) * .14),int((Y2 - Y1) * .66)]
        rl2,gl2,bl2 = pix[int((X2 - X1) * .15),int((Y2 - Y1) * .66)]
        rl3,gl3,bl3 = pix[int((X2 - X1) * .16),int((Y2 - Y1) * .66)]
        rr,gr,br = pix[int((X2 - X1) * .86),int((Y2 - Y1) * .66)]
        rr2,gr2,br2 = pix[int((X2 - X1) * .85),int((Y2 - Y1) * .66)]
        rr3,gr3,br3 = pix[int((X2 - X1) * .84),int((Y2 - Y1) * .66)]
        rm,gm,bm = pix[int((X2 - X1) * .465),int(redY)]

        rlt = rl + rl2 + rl3
        glt = gl + gl2 + gl3
        blt = bl + bl2 + bl3
        rrt = rr + rr2 + rr3
        grt = gr + gr2 +gr3
        brt = br + br2 + br3
        
        if rm < 200:
            print('catch')
            pydirectinput.press('enter')
            fish = False
            time.sleep(9)
        elif(rlt > baserl + 50 or glt > basegl + 50 or blt > basebl + 50):
            print('L')
            # im.save('l.png')
            pydirectinput.press(goleft)
            time.sleep(.4)
        elif(rrt > baserr + 50 or grt > basegr + 50 or brt > basebr + 50):
            print('R')
            # im.save('r.png')
            pydirectinput.press(goright)
            time.sleep(.4)

    try:
        line = logfile.readline()
    except:
        line = None
    print(line)
    while line:
        try:
            line = logfile.readline()
        except:
            line = None
        print(line)
        if fishToCatch in line:
            wait = False

    if wait:
        prevHour = int(content.text[len(content.text) - 8:len(content.text) - 6])
        print('wait: ' + str(prevHour))
        shouldWaitCount = 0
    while(wait and waitEver):
        hourDigit = int(content.text[len(content.text) - 8:len(content.text) - 6])

        if hourDigit != prevHour:
            print(hourDigit)
            if hourDigit == 0 or hourDigit == 4 or hourDigit == 6 or hourDigit == 7 or hourDigit == 17 or hourDigit == 18 or hourDigit == 20:
                wait = False
        prevHour = hourDigit

        try:
            line = logfile.readline()
        except:
            line = None
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        print(line)

        if fishToCatch in line:
            wait = False
