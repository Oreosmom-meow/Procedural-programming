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
        elif self.dest == self.bottom:
            print('Already in the bottom')
        elif self.dest == self.top:
            print('Already in the top')
    def floor_up(self,dest):
        self.dest = int(dest) + 1
        for i in range(self.current_floor,self.dest):
            print(f'Moved to floor {i}')
            self.current_floor = self.dest
        return
    def floor_down(self,dest):
        self.dest = int(dest)
        for i in reversed(range(self.dest, (self.current_floor - 1))):
            self.current_floor = self.dest
            print(f'Moved to floor {i}')
        return
Game_status = True
while Game_status:
    bottom = input('Please input 1 numbers to set up the bottom floor of the elevator: ')
    top = input('Please input 1 numbers to set up the top floor of the elevator: ')
    if int(bottom) < 0 or int(top) < 0:
        print('Please enter positive numbers')
    elif int(bottom) >= int(top):
        print('Please enter bigger top than bottom numbers')
    else:
        h = Elevator(bottom, top)
        print(f'Elevator bottom floor confirmed as {h.bottom}, top floor confirmed as {h.top}')
        floor_list = []
        for i in range(h.bottom, h.top + 1):
            floor_list.append(i)
        for i in floor_list:
            destination = int(input('Please input your numbers to go to: '))
            if destination not in floor_list:
                print(f'Elevator floor does not exist. Game over.')
                Game_status = False
                break
            else:
                h.go_to_floor(destination)

