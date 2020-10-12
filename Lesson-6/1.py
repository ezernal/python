from time import sleep
class TrafficLight:
    __color = ["Красный", "Желтый", "зеленый"]

    def running(self):
        i = 0
        while i < 3:
            print(f"Сетофор загорится {TrafficLight.__color[i]}")
            i += 1
            if i == 1:
                sleep(7)
            elif i == 2:
                sleep(5)
            elif i == 3:
                sleep(3)

trafficLight_1 = TrafficLight()
trafficLight_1.running()