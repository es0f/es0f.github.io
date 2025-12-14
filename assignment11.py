#1
class Publication:
    def __init__(self, name):
        self.name = name
class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author= author
        self.pages = pages
    def print_information(self):
        print(f"Book: {self.name}, Author: {self.author}, Pages: {self.pages}")
class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        print(f"Magazine: {self.name}, Chief editor: {self.chief_editor}")
# main
Magazine("Donald Duck", "Aki Hyyppä").print_information()
Book("Compartment No. 6", "Rosa Liksom", 192).print_information()
#2
#1
class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def Accel(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed
class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery_capacity):
        super().__init__(reg_number, max_speed)
        self.battery_capacity = battery_capacity
class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, tank_volume):
        super().__init__(reg_number, max_speed)
        self.tank_volume = tank_volume
electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)
electric.Accel(120)
gasoline.Accel(100)
electric.drive(3)
gasoline.drive(3)
print("Electric car kilometer counter:", electric.travelled_distance, "km")
print("Gasoline car kilometer counter:", gasoline.travelled_distance, "km")
