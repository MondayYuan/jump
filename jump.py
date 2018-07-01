import os
import cv2
import time

def isRed(BGR):
    B, G, R = BGR
    if(abs(R-255)<15 and G < 100 and B < 100):
        return True
    else:
        return False

k = 2.005
cv2.namedWindow('jump')

while(True):
    os.system('adb shell screencap -p /sdcard/1.png')
    os.system('adb pull /sdcard/1.png 1.png')

    img = cv2.imread('1.png')

    head_y = 1165
    bottom_y = 1250

    for x in range(0,1080):
        if(isRed(img[head_y][x])):
            head_x = x + 8
            break
    for x in range(head_x + 40, 1080):
        if(isRed(img[bottom_y][x])):
            bottom_left = x
            if(not isRed(img[bottom_y][x + 20])):
                bottom_right = x + 16
            else:
                for x in range(x+20, 1080):
                    if(isRed(img[y][x])):
                        continue
                    bottom_right = x
                    break
            bottom_x = (bottom_right + bottom_left)//2
            break
    cv2.circle(img, (bottom_x, bottom_y),15, (0,0,0))
    cv2.circle(img, (head_x, head_y), 15, (0, 0, 0))
    cv2.imshow('jump', cv2.resize(img, (400, 600)))
    cv2.waitKey(200)
    tapTime = int(k * (bottom_x - head_x))
    print(tapTime)
    os.system('adb shell input swipe 540 600 550 610 {0}'.format(tapTime))
    time.sleep(3)

