from util import rgb

class StripeCtrl:
    def __init__(self, strip):
        self._cols = []
        self._widths = []
        self._interval = 1
        self._totalWidth = 0
        self._offset = 0
        self._frames = 0

        self._strip = strip

    def start(self,colors, interval):
        cols = []
        widths = []
        self._totalWidth = 0

        for stripe in colors:
            widths.append(int(stripe['width']))
            cols.append(rgb(stripe['color']))
            self._totalWidth += int(stripe['width'])

        self._offset = 0
        self._interval = interval
        self._frames = 0

        self._cols = cols
        self._widths = widths

    def draw(self):
        if self._frames <= 0:
            self._frames = self._interval * 60
            self._offset += 1
            if self._offset >= self._totalWidth:
                self._offset = 0
            i = -self._offset
            if self._totalWidth > 0:
                while i < len(self._strip):
                    for j, col in enumerate(self._cols):
                        for x in range(self._widths[j]):
                            if i >= 0 and i < len(self._strip):
                                self._strip[i] = col
                            i += 1
                self._strip.show()
        self._frames -= 1