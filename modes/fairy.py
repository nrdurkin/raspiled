import random

class FairyCtrl:
    def __init__(self, strip):
        self._count = 20
        self._arr = []
        self._min_speed = .5
        self._max_speed = 5
        self._strip = strip

    def start(self, min_speed=.5, max_speed=5, count=30):
        self._count = count
        self._max_speed = max_speed
        self._min_speed = min_speed
        self._arr = []
        for i in range(len(self._strip)):
            self._strip[i] = (0, 0, 0)
        for i in range(self._count):
            pos = random.randint(0, len(self._strip) - 1)
            brightness = random.random() * 255 * 2
            speed = random.uniform(min_speed, max_speed)
            self._arr.append([pos, brightness, speed])

    def draw(self):
        for i, light in enumerate(self._arr):
            light[1] += light[2]
            if light[1] > 255 * 2:
                # reset pixel
                self._strip[light[0]] = (0, 0, 0)
                # generate new light
                pos = random.randint(0, 299)
                speed = random.uniform(self._min_speed, self._max_speed)
                self._arr[i] = [pos, 0, speed]
            else:
                x = light[1]
                col = (x, x, x) if x <= 255 else (510 - x, 510 - x, 510 - x)
                self._strip[light[0]] = col
        self._strip.show()
