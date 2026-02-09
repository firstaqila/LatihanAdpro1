class Calculator:
    def add(self, a, b):
        return a + b

    def branch_subtract(self, a, b):
        return a - b

    def branch_multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

if __name__ == "__main__":
    calc = Calculator()

    print("Addition:", calc.add(10, 5))
    print("Subtraction:", calc.subtract(10, 5))
    print("Multiplication:", calc.branch_multiply(10, 5))
    print("Division:", calc.divide(10, 5))
