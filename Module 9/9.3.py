class Car:
    def __init__(self, regi_number, max_speed, speed, trave_distance):
        self.regi_number = regi_number
        self.max_speed = max_speed
        self.speed = speed
        self.trave_distance = trave_distance
        Car.speed = self.speed
        Car.distance = trave_distance
    def accelerate(self, change_of_speed):
        self.change_of_speed = change_of_speed
        self.speed = self.change_of_speed + self.speed
    def brake(self):
        Car.speed = -200
        print(f'The car has been forced to stop at the speed of {Car.speed}')
        return
    def drive(self,time):
        self.time = time
        change_of_distance = self.time * self.speed
        self.trave_distance = change_of_distance + self.trave_distance
        return

new_car = Car("ABC-123", "142",60, 0)
print(f"The new car has registration number of {new_car.regi_number}, max speed at {new_car.max_speed} km/h, current speed at {new_car.speed} km/h, travel distance of {new_car.trave_distance} km.")

if Car.speed < 0:
    new_car.brake()
while Car.speed >= 0:
    print(f'---------------')
    new_speed = int(input("Please input number to accelerate the new car: "))
    new_car.accelerate(new_speed)
    print(f"The current speed is {new_car.speed} km/h.")
    if int(new_car.speed) >= int(new_car.max_speed):
        print("The cars has exceed max speed. Emegency brake activated.")
        new_car.brake()
        break
    else:
        time = int(input("Please input time to drive the new car: "))
        new_car.drive(time)
        print(f'The car has traveled to {new_car.trave_distance} km within the {time}h you input.')

