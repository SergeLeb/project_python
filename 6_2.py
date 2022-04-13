class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, weigth=25, thickness=5):
        return self._length * self._width * weigth * thickness / 1000

r = Road(20, 10000)
print(r.mass())
