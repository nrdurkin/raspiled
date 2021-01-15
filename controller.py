import time, random

import board, colorsys, neopixel


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
    frame(0)


def frame(fadeHue=0):
    if mode == 'CROSSFADE':
        fadeHue+=.005
        if fadeHue >1:
            fadeHue = 0
        strip.fill(colorsys.hls_to_rgb(fadeHue,.5,1))
        time.sleep(.05)
        frame(fadeHue)
    else:
        return

                # blockColor(strip, rgb(color))  # Green wipe

    # except KeyboardInterrupt:
    #     colorWipe(strip, (0, 0, 0), 10)

fairyVar = {
    'lights':20,
    'arr':[]
}

def initFairy():
    global mode
    mode = 'FAIRY'
    fairyVar['lights'] = 20
    for i in range(fairyVar['lights']):
        print(i)
        pos = random.randint(0,299)
        brightness = random.random()*255*2
        speed = random.random()*5+.1
        print([pos, brightness, speed])
        fairyVar['arr'] = [pos, brightness, speed]

def drawFairy():
    for i, light in enumerate(fairyVar['arr']):
        print(light[1], light[2])
        light[1] += light[2]
        if light[1] > 255*2:
            #reset pixel
            strip[light[0]] = rgb(0,0,0)
            #generate new light
            pos = random.randint(0, 299)
            speed = random.random()*5+.1
            fairyVar['arr'][i] = [pos, 0, speed]
        else:
            x = light[1]
            col = rgb(x,x,x) if x <= 255 else rgb(510-x,510-x,510-x)
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
    loop()
    currentTime = time.time()
    sleepTime = 1. / FPS - (currentTime - lastFrameTime)
    lastFrameTime = currentTime
    if sleepTime > 0:
        time.sleep(sleepTime)
    main(lastFrameTime)


# each mode can have state object and function
# master loop checks mode, calls function
# function calculates next frame and draws it, updating state object

# either one init function, or each mode can have its own init function
