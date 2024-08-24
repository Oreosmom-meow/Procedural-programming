class car:
    def __init__(self, regi_number, max_speed, current_speed, trave_distance):
        self.regi_number = regi_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.trave_distance = 0
    def print_value(self):
        print(f"The new car has registration number of {self.regi_number}, max speed at {self.max_speed} km/h, current speed at {self.current_speed} km/h, travel distance of {self.trave_distance} km.")

new_car = car("ABC-123", "142",0, 0)
new_car.print_value()       