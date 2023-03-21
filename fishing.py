import pyscreenshot as ImageGrab
import cv2
import pytesseract
from PIL import Image
import time
from skimage import util
import pydirectinput
import random

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

goleft = 'a'
goright = 'd'
end = 999999999
count = 0
waitcount = 0
waitFirst = False
time.sleep(5)

begin = time.time()

while(2>1):
    searching = True
    fish = True
    logout=False
    prevHour = 99
    wait=False
    lasttime = time.time()

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
        im = ImageGrab.grab(bbox=(23, 1332, 700, 1374))  # X1,Y1,X2,Y2
        im.save('screenshot.png')
        img = cv2.imread('screenshot.png')
        img2 = util.invert(img)
        img3 = Image.fromarray(img2, 'RGB')
        text = pytesseract.image_to_string(img3)
        print(text)
        laptime = round((time.time() - lasttime), 2)
        if(laptime > 25):
            searching = False
            fish = False
            count = 0
            pydirectinput.press('esc')
            time.sleep(random.randint(4,6))
        if ("have a good feeling" in text or "senses tell you that this" in text) and "Nohrin caught a" not in text:
            fish = True
            searching = False
            count = 0
            waitcount = 0
        elif "!!!" in text or "strength.." in text or "ferociously" in text or "have a terrible" in text or  "have a bad" in text or  "You didn't catch anything" in text or "reel this one in" in text:
            fish = False
            searching = False
            count = 0
            time.sleep(1)
            pydirectinput.press('esc')
            time.sleep(random.randint(5,6))
            pydirectinput.press('/')
            pydirectinput.press('c')
            pydirectinput.press('l')
            pydirectinput.press('o')
            pydirectinput.press('c')
            pydirectinput.press('k')
            pydirectinput.press('enter')
            time.sleep(1)
        if "fish without bait" in text or "Nohrin regretfully" in text or "cannot fish here" in text:
            count = count + 1
            searching = False
            logout=True
        if "pulling at" in text:
            fish = False
            searching = False
            wait = True
            count = 0
            waitcount = waitcount + 1
            time.sleep(1)
            pydirectinput.press('esc')
            time.sleep(random.randint(5,6))
            pydirectinput.press('/')
            pydirectinput.press('c')
            pydirectinput.press('l')
            pydirectinput.press('o')
            pydirectinput.press('c')
            pydirectinput.press('k')
            pydirectinput.press('enter')
            time.sleep(1)

    totaltime = round((time.time() - begin), 2)

    if(logout == True or totaltime > end):
        # if count < 3:
        #     pydirectinput.press('/')
        #     pydirectinput.press('e')
        #     pydirectinput.press('q')
        #     pydirectinput.press('u')
        #     pydirectinput.press('i')
        #     pydirectinput.press('p')
        #     pydirectinput.press('s')
        #     pydirectinput.press('e')
        #     pydirectinput.press('t')
        #     pydirectinput.press('space')
        #     pydirectinput.press('1')
        #     pydirectinput.press('enter')
        #     logout = False
        # else:
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
        im = ImageGrab.grab(bbox=(200, 300, 2400, 800)) 
        im.save('catch.png')
        pix = im.load()

        rl,gl,bl = pix[364,284]
        rr,gr,br = pix[1800,300]
        rm,gm,bm = pix[1009,12]
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
            time.sleep(.3)
        if(rr > 105 or br > 105 or gr > 105):
            print('R')
            lasttime = time.time()
            pydirectinput.press(goright)
            time.sleep(.3)
        
        if rm < 200:
            pydirectinput.press('enter')
            fish = False
            time.sleep(1)
            im = ImageGrab.grab(bbox=(23, 1352, 700, 1374))  # X1,Y1,X2,Y2
            im.save('screenshot.png')
            img = cv2.imread('screenshot.png')
            img2 = util.invert(img)
            img3 = Image.fromarray(img2, 'RGB')
            text = pytesseract.image_to_string(img3)
            print(text)
            time.sleep(random.randint(5,6))

    # lasttime = time.time()

    # timetowait = 10

    # while(wait):
    #     laptime = round((time.time() - lasttime), 2)

    #     im = ImageGrab.grab(bbox=(23, 1332, 700, 1374))  # X1,Y1,X2,Y2
    #     im.save('screenshot.png')
    #     img = cv2.imread('screenshot.png')
    #     img2 = util.invert(img)
    #     img3 = Image.fromarray(img2, 'RGB')
    #     text = pytesseract.image_to_string(img3)
    #     print(text)

    #     if "tiger" in text or "carp" in text:
    #         wait = False
    #     elif laptime > timetowait:
    #         pydirectinput.press('/')
    #         pydirectinput.press('c')
    #         pydirectinput.press('l')
    #         pydirectinput.press('o')
    #         pydirectinput.press('c')
    #         pydirectinput.press('k')
    #         pydirectinput.press('enter')
    #         time.sleep(1)
    #         im = ImageGrab.grab(bbox=(300, 1310, 500, 1333))  # X1,Y1,X2,Y2
    #         im.save('screenshottime.png')
    #         img = cv2.imread('screenshottime.png')
    #         img2 = util.invert(img)
    #         img3 = Image.fromarray(img2, 'RGB')
    #         text = pytesseract.image_to_string(img3, config = '--psm 13 --oem 3')
    #         print(text)
    #         if len(text) > 4 and ',' in text and ':' in text:
    #             hourString = text[text.index(',')+2:text.index(':')]
    #             print(hourString)
    #             if hourString.isdigit():
    #                 hour = int(hourString)
    #                 if prevHour == 99:
    #                     prevHour = hour
    #                     if hour > 7 and hour < 16:
    #                         timetowait = 120 * (17 - hour)
    #                     else:
    #                         timetowait = random.randint(5,20)
    #                 if hour != prevHour:
    #                     if hour == 0 or hour == 4 or hour == 6 or hour == 7 or hour == 17 or hour == 18 or hour == 20:
    #                         wait = False
    #                     if hour > 7 and hour < 16:
    #                         timetowait = 120 * (17 - hour)
    #                     else:
    #                         timetowait = random.randint(5,20)
    #                 prevHour = hour
            
    #         lasttime = time.time()
