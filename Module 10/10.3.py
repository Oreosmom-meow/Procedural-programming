class Elevator:
    def __init__(self,bottom,top):
        self.bottom = int(bottom)
        self.top = int(top)
        self.current_floor = self.bottom
    def go_to_floor(self,dest):
        self.dest = int(dest)
        if self.dest > self.current_floor:
            self.floor_up(self.dest)
        elif self.dest < self.current_floor:
            self.floor_down(self.dest)
        elif self.dest == self.current_floor:
            print('No change on floor.')
            
    def floor_up(self,dest):
        self.dest = int(dest)
        for i in range((self.current_floor + 1),(self.dest + 1)):
            self.current_floor = self.dest
            print(f'Moved to floor {i}')
        return
    def floor_down(self,dest):
        self.dest = int(dest)
        for i in reversed(range(self.dest, (self.current_floor))):
            print(f'Moved to floor {i}')
            self.current_floor = self.dest
        return

class Building:
    def __init__(self,bottom,top,elevator_number):
        self.bottom = int(bottom)
        self.top = int(top)
        self.elevator_number = int(elevator_number)
        self.elevator_list = []
        for i in range(1, (self.elevator_number + 1)):
            self.elevator_list.append(i)
            self.elevator = Elevator(self.bottom,self.top)
    def run_elevator(self, elevator_number, destination):
        self.elevator_number = int(elevator_number)
        self.destination = int(destination)
        self.elevator.go_to_floor(self.destination)
        return
    def fire_alarm(self):
        print(f'Fire alarm activated')
        self.elevator.floor_down(self.elevator.bottom)
        
Game_status = False
while Game_status is False:
    bottom = input('Please input 1 numbers to set up the bottom floor of the elevator: ')
    top = input('Please input 1 numbers to set up the top floor of the elevator: ')
    elevator_number = input('Please input the number of elevators you want to create: ')
    if int(bottom) < 0 or int(top) < 0:
        print('Please enter positive numbers')
    elif int(bottom) >= int(top):
        print('Please enter bigger top than bottom numbers')
    elif bottom == '' or top == '' or elevator_number == '':
        print(f'Please input a number to start the evelator.')
    else:
        h = Building(bottom, top, elevator_number)
        print(f'Elevator bottom floor confirmed as {h.bottom}, top floor confirmed as {h.top}, you created {h.elevator_number} elevators in the building. Evelator start from floor {h.bottom}')
        Game_status = True

while Game_status is True:
    floor_list = []
    for g in range(h.bottom, h.top + 1):
        floor_list.append(g)
    ele_number = int(input(f'Input number of elevator you want to run: '))
    if int(ele_number) not in h.elevator_list:
        print('Please enter a valid elevator number.')
        break
    else:
        while ele_number in h.elevator_list:
            print(f'Elevator number {ele_number} is running now.')
            destination = input('Please input your floor numbers to go to: ')
            if destination == 'fire':
                h.run_elevator(ele_number, destination)
                destination = input('Please input your numbers to go to: ')
            elif int(destination) not in floor_list:
                print(f'Elevator floor does not exist. Start from beginning.')
                Game_status = False
                break
            else:
                while int(destination) in floor_list:
                    h.run_elevator(ele_number, destination)
                    destination = input('Please input your numbers to go to: ')
                    if destination == 'fire':
                        h.fire_alarm()
                        break