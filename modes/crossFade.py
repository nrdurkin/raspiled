import random
from util import randomPrettyRGB

class CrossFadeCtrl:
    def __init__(self, fill):
        self._col = []
        self._change = []
        self._frames = 0
        self._fill = fill

        self._start()

    def _getNext(self):
        self._col[0] = int(self._col[0])
        self._col[1] = int(self._col[1])
        self._col[2] = int(self._col[2])
        new_rgb = randomPrettyRGB()
        frames = random.randint(120, 360)
        dR = float(new_rgb[0] - self._col[0]) / frames
        dG = float(new_rgb[1] - self._col[1]) / frames
        dB = float(new_rgb[2] - self._col[2]) / frames
        self._change = [dR, dG, dB]
        self._frames = frames

    def draw(self):
        col = tuple(self._col)
        self._col[0] += self._change[0]
        self._col[1] += self._change[1]
        self._col[2] += self._change[2]
        self._frames -= 1
        self._fill(col)
        if self._frames <= 0:
            self._getNext()

    def _start(self):
        self._col = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self._getNext()