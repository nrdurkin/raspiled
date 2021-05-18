from util import randomPrettyRGB
import random

class Node:
    def __init__(self, index):
        self.index = index
        self.color = randomPrettyRGB()
        self.life = random.randint(60*4, 60*10)

class RippleCtrl:
    def __init__(self,strip):
        self._node = []
        self._colors = [(0,0,0) for i in range(len(strip))]
        self._strip = strip

    def start(self):
        self._node.append(Node(random.randint(0,len(self._strip))))

    def _averageLocal(self, i):

        f = lambda q:-.03 * q * q + 1

        start = max(i-5, 0)
        end = min(i+5, len(self._strip))

        r = g = b = t = 0
        for x in range(start, end):
            c = self._colors[x]
            weight = f(x-i)
            r+=c[0] * weight
            g+=c[1]* weight
            b+=c[2]* weight
            t += weight

        return r/t, g/t, b/t

    def draw(self):
        newCols = []
        for i in range(self._colors):
            newCols[i] = self._averageLocal(i)
        self._colors = newCols
        for i, col in enumerate(self._colors):
            self._strip[i] = col
