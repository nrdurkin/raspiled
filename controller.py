import time, random

import board, neopixel, colorsys


# LED strip configuration:
LED_COUNT = 300  # Number of LED pixels.
strip = neopixel.NeoPixel(board.D18, LED_COUNT, auto_write=False)
mode = ''

def fill(color):
    for i in range(LED_COUNT):
        strip[i] = color
    strip.show()

def randomPrettyRGB():
    percent = colorsys.hsv_to_rgb(random.uniform(0, 1), 1, 1)
    return (255*percent[0], 255*percent[1], 255*percent[2])

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
    fadeVar['col'][0] = int(fadeVar['col'][0])
    fadeVar['col'][1] = int(fadeVar['col'][1])
    fadeVar['col'][2] = int(fadeVar['col'][2])
    new_rgb = randomPrettyRGB()
    frames = random.randint(120,360)
    dR = float(new_rgb[0] - fadeVar['col'][0]) / frames
    dG = float(new_rgb[1] - fadeVar['col'][1]) / frames
    dB = float(new_rgb[2] - fadeVar['col'][2]) / frames
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

stripeVar = {
    'col' : [],
    'width' : [],
    'interval' : 1,
    'totalWidth' : 0,
    'offset' : 0,
    'frames' : 0
}

def initStripe():
    global mode
    mode = 'STRIPE'
    colors = [], widths = []
    colors.append((255,0,0))
    colors.append((0,255,0))
    widths.append(2)
    widths.append(2)

    stripeVar['totalWidth'] = 4
    stripeVar['offset'] = 0
    stripeVar['interval'] = 1
    stripeVar['frames'] = 0

    stripeVar['col'] = colors, stripeVar['width'] = widths

def drawStripe():
    if stripeVar['frames'] <=0:
        stripeVar['frames'] = stripeVar['interval'] * 60
        stripeVar['offset'] += 1
        if stripeVar['offset'] > stripeVar['totalWidth']:
            stripeVar['offset'] = 0
        i = 0
        while i < LED_COUNT:
            for j, col in enumerate(stripeVar['colors']):
                for x in range(stripeVar['width'][j]):
                    strip[i] = col
                    i+=1
        strip.show()
    stripeVar['frames'] -= 1

def loop():
    global mode
    if mode == 'FAIRY':
        drawFairy()
    elif mode == 'CROSSFADE':
        drawCrossFade()
    elif mode == 'STRIPE':
        drawStripe()
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
