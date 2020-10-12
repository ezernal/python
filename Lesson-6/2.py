class Road:
    def __init__(self, _lenght, _width, _volume):
        self._lenght = _lenght
        self._width = _width
        self._volume = _volume
    def mass(self):
        return self._lenght * self._width * self._volume

class MassCount(Road):
    def __init__(self, _lenght, _width, _volume):
        super().__init__(_lenght, _width, _volume)


a = MassCount(125, 5000, 15)
print(a.mass())