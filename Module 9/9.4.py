import random

class Car:
    rounds = 0
    def __init__(self, regi_number, max_speed, speed, trave_distance):
        self.regi_number = regi_number
        self.max_speed = max_speed
        self.speed = speed
        self.trave_distance = trave_distance
        Car.speed = self.speed
        Car.distance = trave_distance
    def accelerate(self):
        speed_change = random.randint(-10, 15)
        self.speed += speed_change
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.max_speed:
            self.speed = self.max_speed
    def brake(self):
        Car.speed = -200
        print(f'The car has been forced to stop at the speed of {Car.speed}')
        return

    def drive(self):
        self.trave_distance += self.speed

car_list = []
for i in range(11):
    random_name = 'ABC' + '-' + str(i)
    max_speed = random.randint(100, 200)
    speed = 0
    distance = 0
    car = Car(random_name, max_speed, speed, distance)
    car_list.append(car)

race_finished = False
while not race_finished:
    for car in car_list:
        car.accelerate()
        Car.rounds += 1
        car.drive()
        if car.trave_distance >= 10000:
            race_finished = True
            break

print(f'Game finishes after {Car.rounds} hours.')
print(f"{'Car':<10} {'Max Speed (km/h)':<20} {'Final Speed (km/h)':<20} {'Distance Traveled (km)':<25}")
print("-" * 75)
for car in car_list:
    print(f"{car.regi_number:<10} {car.max_speed:<20} {car.speed:<20} {car.trave_distance:<25}")


