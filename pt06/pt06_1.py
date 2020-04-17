from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        while True:
            print(TrafficLight.__color[0])
            sleep(7)
            print(TrafficLight.__color[1])
            sleep(2)
            print(TrafficLight.__color[2])
            sleep(7)


tl = TrafficLight()
tl.running()