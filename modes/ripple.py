from util import randomPrettyRGB
import random

class Node:
    def __init__(self, index):
        self.index = index
        self.color = randomPrettyRGB()
        self.life = random.randint(60*4, 60*10)

class RippleCtrl:
    def __init__(self,strip):
        self._nodes = []
        self._colors = [(0,0,0) for i in range(len(strip))]
        self._strip = strip

    def start(self):
        self._nodes.append(Node(10))

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

        if i == 10:
            print(r/t, g/t, b/t)

        return r/t, g/t, b/t

    def draw(self):

        for node in self._nodes:
            max_change = 7
            cur = self._colors[node.index]
            tar = node.color
            r = max(max_change, min(-max_change, tar[0] - cur[0]))
            g = max(max_change, min(-max_change, tar[1] - cur[1]))
            b = max(max_change, min(-max_change, tar[2] - cur[2]))
            self._colors[node.index] = (r,g,b)
            print(self._colors[node.index])


        newCols = []
        for i in range(len(self._colors)):
            newCols.append( self._averageLocal(i))
        self._colors = newCols
        for i, col in enumerate(self._colors):
            self._strip[i] = col
