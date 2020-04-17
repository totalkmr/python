class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} начал движение.')

    def stop(self):
        print(f'Автомобиль {self.name} остановился.')

    def turn(self, direction):
        self.direction = direction
        print(f'Автомобиль {self.name} повернул {self.direction}.')

    def show_speed(self):
        print(f'Текущая корость движения автомобиля {self.name} составляет {self.speed} км/ч.')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая корость движения автомобиля {self.name} составляет {self.speed} км/ч.')
        if self.speed > 60:
            print('Внимание! Превышение скорости!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая корость движения автомобиля {self.name} составляет {self.speed} км/ч.')
        if self.speed > 40:
            print('Внимание! Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(30, 'yellow', 'Nissan', False)
sport_car = SportCar(100, 'white', 'Ferrari', False)
work_car = WorkCar(70, 'red', 'Reno', False)
police_car = PoliceCar(50, 'blue', 'Lada', True)

town_car.go()
sport_car.turn('направо')
work_car.turn('налево')
police_car.stop()
work_car.show_speed()