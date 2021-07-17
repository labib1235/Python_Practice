

class Bike:

    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print("name:", self.name)
        print("color:", self.color)
        print("Starting the engine")

my_bike1 = Bike("Repsol", "Orange")
my_bike1.start()
my_bike2 = Bike("Yamaha MT-15", "Black")
my_bike2.start()
my_bike3 = Bike("Harley Davidson GIOTTO 5", "Black")
my_bike3.start()








