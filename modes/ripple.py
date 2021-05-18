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

        f = lambda q: 1 if q == 0 else 0

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

        for node in self._nodes:
            max_change = 7
            cur = self._colors[node.index]
            tar = node.color
            r = cur[0] + max(-max_change, min(max_change, tar[0] - cur[0]))
            g = cur[1] + max(-max_change, min(max_change, tar[1] - cur[1]))
            b = cur[2] + max(-max_change, min(max_change, tar[2] - cur[2]))
            self._colors[node.index] = (r,g,b)


        newCols = []
        for i in range(len(self._colors)):
            newCols.append(self._averageLocal(i))
        self._colors = newCols
        print(self._colors[10])
        for i, col in enumerate(self._colors):
            self._strip[i] = self._colors[10]
