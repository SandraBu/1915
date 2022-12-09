class human:
    def __init__ (self, name = "human"):
        self.name = name
class Auto:
    def __init__ (self, brand):
        self.brand = brand
        self.pas = []
    def add_pas(self, human):
        self.pas.append(human)
    def print_pas_names (self):
        if self.pas != []:
            print(f"names of {self.brand} pas:")
            for pas in self.pas:
                print(pas.name)
        else:
            print(f"There no passengers in {self.brand}")
Max = human("Maxim")
Sviatoslav = human("Sviatoslav")
Maxim = human("Maxim")
car = Auto("Mini")
car.add_pas(Max)
car.add_pas(Sviatoslav)
car.add_pas(Maxim)
car.print_pas_names()
car1 = Auto("Tesla")
car1.print_pas_names()
