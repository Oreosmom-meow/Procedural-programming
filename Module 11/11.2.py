import random


class Car:
    hour = 0

    def __init__(self, regi_number, max_speed):
        self.regi_number = regi_number
        self.max_speed = max_speed
        self.speed = 60
        self.trave_distance = 0

    def accelerate(self):
        speed_change = random.randint(-10, 15)
        self.speed += speed_change
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.max_speed:
            self.speed = self.max_speed

    def brake(self):
        self.speed = -200
        print(f"The car has been forced to stop at the speed of {self.speed}")
        return

    def drive(self, time):
        self.trave_distance = time * self.speed
        print(f"Traveled {self.trave_distance}")


class EletricCar(Car):

    def __init__(self, regi_number, max_speed, battery):
        self.battery = battery
        super().__init__(regi_number, max_speed)

    def drive(self, time):
        print("Eletric car")
        super().drive(time)


class GasolineCar(Car):

    def __init__(self, regi_number, max_speed, volume):
        self.volume = volume
        super().__init__(regi_number, max_speed)

    def drive(self, time):
        print("Gasoline Car")
        super().drive(time)


new_electic_car = EletricCar("ABC-15", 180, 52.5)
new_gasoline_car = GasolineCar("ACD-123", 165, 32.3)

new_electic_car.drive(3)
new_gasoline_car.drive(3)
