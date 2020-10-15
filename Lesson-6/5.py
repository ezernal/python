class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f"Запуск отрисовки {self.title}")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"Ручка пишет {self.title}"

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"Карандаш рисует {self.title}"

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"Маркер подчеркивает {self.title}"

pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())