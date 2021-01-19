import time, random

import board, neopixel


# LED strip configuration:
LED_COUNT = 300  # Number of LED pixels.
strip = neopixel.NeoPixel(board.D18, LED_COUNT, auto_write=False)

def fill(color):
    for i in range(LED_COUNT):
        strip[i] = color
    strip.show()

fill((255,0,0))
time.sleep(.3)
fill((0,255,0))
time.sleep(.3)
fill((0,0,255))
time.sleep(.3)
fill((0,0,0))

def blockColor(color):
    global mode
    mode = 'BLOCK'
    fill(color)

def rgb(hex):
    if hex[0] == '#':
        hex = hex[1:]
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))

fadeVar = {
    'col':[],
    'change':[],
    'frames' : 0
}

def nextCrossFade():
    fadeVar['col'][0] = int(fadeVar['col'[0]])
    fadeVar['col'][1] = int(fadeVar['col'[1]])
    fadeVar['col'][2] = int(fadeVar['col'[2]])
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    frames = random.randint(120,360)
    dR = float(r - fadeVar['col'][0]) / frames
    dG = float(g - fadeVar['col'][1]) / frames
    dB = float(b - fadeVar['col'][2]) / frames
    fadeVar['change'] = [dR,dG,dB]
    fadeVar['frames'] = frames

def initCrossFade():
    global mode
    mode = 'CROSSFADE'
    fadeVar['col'] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    nextCrossFade()

def drawCrossFade():
    col = tuple(fadeVar['col'])
    fadeVar['col'][0]+=fadeVar['change'][0]
    fadeVar['col'][1] += fadeVar['change'][1]
    fadeVar['col'][2]+=fadeVar['change'][2]
    fadeVar['frames'] -= 1
    fill(col)
    if fadeVar['frames'] <=0:
        nextCrossFade()

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
    for i in range(LED_COUNT):
        strip[i] = (0,0,0)
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

def loop():
    global mode
    if mode == 'FAIRY':
        drawFairy()
    elif mode == 'CROSSFADE':
        drawCrossFade()
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
