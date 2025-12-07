#1
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom
    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
        print(f"Elevator is at floor {self.current_floor}")
    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
        print(f"Elevator is at floor {self.current_floor}")
    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
#2
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))
    def run_elevator(self, elevator_number, targeted_floor):
        self.elevators[elevator_number].go_to_floor(targeted_floor)
#3
    def fire_alarm(self):
        print("Alarm")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)
def main_program():
    a = Elevator(1, 10)
    a.go_to_floor(2)
main_program()
def main2():
    b = Building(1, 10, 3)
    b.run_elevator(2, 4)
main2()
def main3():
    c = Building(1, 10, 2)
    c.run_elevator(1, 4)
    c.fire_alarm()
main3()


