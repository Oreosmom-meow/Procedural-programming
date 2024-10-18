class car:
    def __init__(self, regi_number, max_speed, current_speed, trave_distance):
        self.regi_number = regi_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.trave_distance = trave_distance
    #def print_value(self):
        #print(f"The new car has registration number of {self.regi_number}, max speed at {self.max_speed} km/h, current speed at {self.current_speed} km/h, travel distance of {self.trave_distance} km.")

new_car = car("ABC-123", "142",12, 11)
print(f"The new car has registration number of {new_car.regi_number}, max speed at {new_car.max_speed} km/h, current speed at {new_car.current_speed} km/h, travel distance of {new_car.trave_distance} km.")  