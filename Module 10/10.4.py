import random
class Car:
    hour = 0
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

class Race:
    race_finish = False
    def __init__(self,name,kilometers,car_list):
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list

    def hour_passes(self):
        while self.race_finish == False:
            for car in self.car_list:
                if car.trave_distance >= self.kilometers:
                    self.race_finished()
                    break
                else:
                    car.accelerate()
                    Car.hour += 1
                    car.drive()                

    def print_status(self):
        print(f'Race finished in hour {Car.hour}.')
        print(f"{'Car':<10} {'Max Speed (km/h)':<20} {'Current Speed (km/h)':<20} {'Distance Traveled (km)':<25}")
        print("-" * 75)
        for car in self.car_list:
            print(f"{car.regi_number:<10} {car.max_speed:<20} {car.speed:<20} {car.trave_distance:<25}")

    def race_finished(self):
        for car in self.car_list:
            if car.trave_distance >= self.kilometers:
                self.race_finish = True
                return self.race_finish
            else:
                return False
def generate_car_list():
    car_list = []
    for i in range(11):
        random_name = 'ABC' + '-' + str(i)
        max_speed = random.randint(100, 200)
        speed = 0
        distance = 0
        car = Car(random_name, max_speed, speed, distance)
        car_list.append(car)
    return car_list

race_car_list = generate_car_list()
new_race = Race('Grand Demolition Derby',8000, race_car_list)
while new_race.race_finish == False:
    new_race.hour_passes()
    if new_race.race_finish == True:
        new_race.print_status()
        break 
