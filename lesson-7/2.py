class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height
    def get_palto(self):
        return self.size / 6.5 + 0.5
    def get_costume(self):
        return self.height * 2 + 0.3
    @property
    def get_sum_clothes(self):
        return str(f'Общий рассход \n'
            f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Palto(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.palto = self.size / 6.5 + 0.5
    def __str__(self):
        return f"{self.palto}"

class Costume(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.costume = self.height * 2 + 0.3
    def __str__(self):
        return f"{self.costume}"

p = Palto(12, 10)
c = Costume(10, 12)
print(p)
print(c)
print(p.get_sum_clothes)