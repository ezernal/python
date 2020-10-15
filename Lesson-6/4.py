class Car:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction
    def show_speed(self):
        return self.speed
    def go(self):
        return "Машина поехала"
    def stop(self):
        return "Машина остановилась"
    def turn(self):
        return f"Машина повернула {self.direction}"

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            return "Скорость превышена"
        else:
            return self.speed
class SportCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            return "Скорость превышена"
        else:
            return self.speed
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)


audi = SportCar(80, "red", "audi", False, "направо")
bobik = PoliceCar(40, "haki", "bobik", True, "Прямо")
trashcar = WorkCar(50, "black", "trashcar", False, "налево")
oka = TownCar(15, "white", "oka", False, "назад")

print(oka.go())
print(bobik.go())
print(trashcar.show_speed())
print(oka.direction)
print(audi.turn())