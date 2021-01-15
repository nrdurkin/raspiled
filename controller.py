import time, random

import board, neopixel


# LED strip configuration:
LED_COUNT = 300  # Number of LED pixels.
strip = neopixel.NeoPixel(board.D18, LED_COUNT, auto_write=False)

mode = 'BLOCK'

def blockColor(color):
    mode = 'BLOCK'
    for i in range(LED_COUNT):
        strip[i] = color
    strip.show()

def rgb(hex):
    if hex[0] == '#':
        hex = hex[1:]
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))

def crossFade():
    mode = 'CROSSFADE'


fairyVar = {
    'lights':20,
    'arr':[],
    'min_speed':.5,
    'max_speed':5
}

def initFairy(min_speed=.5, max_speed=5, count=30):
    global mode
    mode = 'FAIRY'
    fairyVar['lights'] = count
    fairyVar['max_speed'] = max_speed
    fairyVar['min_speed'] = min_speed
    fairyVar['arr'] = []
    for i in range(fairyVar['lights']):
        pos = random.randint(0,299)
        brightness = random.random()*255*2
        speed = random.uniform(min_speed, max_speed)
        fairyVar['arr'].append([pos, brightness, speed])

def drawFairy():
    for i, light in enumerate(fairyVar['arr']):
        light[1] += light[2]
        if light[1] > 255*2:
            #reset pixel
            strip[light[0]] = (0,0,0)
            #generate new light
            pos = random.randint(0, 299)
            speed = random.uniform(fairyVar['min_speed'], fairyVar['max_speed'])
            fairyVar['arr'][i] = [pos, 0, speed]
        else:
            x = light[1]
            col = (x,x,x) if x <= 255 else (510-x,510-x,510-x)
            strip[light[0]] = col
    strip.show()

frameCount = 0
def loop():
    global frameCount, mode
    frameCount+=1
    if mode == 'FAIRY':

        drawFairy()
    return

FPS = 60
def main(lastFrameTime):
    while True:
        loop()
        currentTime = time.time()
        sleepTime = 1. / FPS - (currentTime - lastFrameTime)
        lastFrameTime = currentTime
        if sleepTime > 0:
            time.sleep(sleepTime)


# each mode can have state object and function
# master loop checks mode, calls function
# function calculates next frame and draws it, updating state object

# either one init function, or each mode can have its own init function
