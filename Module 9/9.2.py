class car:
    def __init__(self, regi_number, max_speed, current_speed, trave_distance):
        self.regi_number = regi_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.trave_distance = 0
    def accelerate(self, change_of_speed):
        self.change_of_speed = change_of_speed
        self.current_speed = self.current_speed + self.change_of_speed
        return
    def brake(self, change_of_speed):
        if self.change_of_speed <= 0:
            print("The car has stopped.")
        return
    def exceed(self, current_speed):
        if int(self.current_speed) >= int(self.max_speed):
            print("The cars has exceed max speed.")
        return

new_car = car("ABC-123", "142",12, 11)
print(f"The new car has registration number of {new_car.regi_number}, max speed at {new_car.max_speed} km/h, current speed at {new_car.current_speed} km/h, travel distance of {new_car.trave_distance} km.")  

new_speed = int(input("Please input number to accelerate the new car: "))
if new_speed < 0:
    new_car.brake(new_speed)
while new_speed >= 0:
    if new_speed < 0:
        new_car.brake(new_speed)
        break
    elif int(new_car.current_speed) >= int(new_car.max_speed):
        new_car.exceed(new_car.current_speed)
        break
    else:
        new_car.accelerate(new_speed)
        print(f"The current speed is {new_car.current_speed} km/h.")
        new_speed = int(input("Please input number to accelerate the new car: "))
