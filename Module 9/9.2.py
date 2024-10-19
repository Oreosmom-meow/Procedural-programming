class Car:
    def __init__(self, regi_number, max_speed, speed, trave_distance):
        self.regi_number = regi_number
        self.max_speed = max_speed
        self.speed = speed
        self.trave_distance = trave_distance
    def accelerate(self, change_of_speed):
        self.change_of_speed = change_of_speed
        self.speed = self.change_of_speed + self.speed

    def brake(self,change_of_speed):
        self.change_of_speed = change_of_speed
        self.speed = self.change_of_speed
        print(f'The car has been forced to stop at the speed of {self.speed}')
        return

new_car = Car("ABC-123", "142",12, 11)
print(f"The new car has registration number of {new_car.regi_number}, max speed at {new_car.max_speed} km/h, current speed at {new_car.speed} km/h, travel distance of {new_car.trave_distance} km.")

new_speed = int(input("Please input number to accelerate the new car: "))
if new_speed < 0:
    new_car.brake(new_speed)
while new_speed >= 0:
    print(f'---------------')
    new_car.accelerate(new_speed)
    if int(new_car.speed) >= int(new_car.max_speed):
        print(f"The current speed is {new_car.speed} km/h.")
        print("The cars has exceed max speed. Emegency brake activated.")
        new_car.brake(-200)
        break
    else:
        print(f"The current speed is {new_car.speed} km/h.")
        new_speed = int(input("Please input number to accelerate the new car: "))
