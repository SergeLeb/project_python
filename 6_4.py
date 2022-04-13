class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is stared'

    def stop(self):
        return f'{self.name} is stopped'

    def turn(self):
        return f'{self.name} is turned right'

    def turn(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'current speed {self.name} is {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'speed of {self.name} is higher than allow for town car'
        else:
            return f'speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return(f'current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'speed of {self.name} is higher than allow for work car'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'

audi = SportCar(160, 'red', 'audi', False)
oka = TownCar(39, 'green', 'oka', False)
lada = WorkCar(80, 'white', 'lada', False)
ford = PoliceCar(100, 'blue', 'ford', True)

print(f'{lada.go()} with speed exactly {lada.show_speed()}')
print(f'{lada.name} is {lada.color}')
print(f'Is {audi.name} a police car? {audi.is_police}')
print(f'Is {lada.name} a police car? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())