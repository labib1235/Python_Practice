class Calculator:
    """Do addition, substraction, multiplication and division."""
    

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def additon(self):
        return self.a + self.b
    def substraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "It is impossible to divide by zero. "

my_calculator = Calculator(90, 10)

temp = my_calculator.additon()
print(temp)

temp = my_calculator.substraction()
print(temp)

temp = my_calculator.multiplication()
print(temp)

temp = my_calculator.division()
print(temp)
