import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error: Square root of negative number is not allowed"
    else:
        return math.sqrt(x)

def log(x):
    if x <= 0:
        return "Error: Logarithm of non-positive number is not allowed"
    else:
        return math.log(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Factorial is only defined for non-negative integers"
    return math.factorial(n)

if __name__ == "__main__":
    print("Advanced Calculator")
    print("1. Basic Operations")
    print("  a. Addition")
    print("  b. Subtraction")
    print("  c. Multiplication")
    print("  d. Division")
    print("2. Exponentiation")
    print("3. Square Root")
    print("4. Logarithm")
    print("5. Trigonometric Functions")
    print("  a. Sine")
    print("  b. Cosine")
    print("  c. Tangent")

    while True:
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == '1':
            print("Basic Operations")
            print("a. Addition")
            print("b. Subtraction")
            print("c. Multiplication")
            print("d. Division")
            basic_choice = input("Enter your choice (a/b/c/d): ")
            if basic_choice in ('a', 'b', 'c', 'd'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if basic_choice == 'a':
                    print(num1, "+", num2, "=", add(num1, num2))
                elif basic_choice == 'b':
                    print(num1, "-", num2, "=", subtract(num1, num2))
                elif basic_choice == 'c':
                    print(num1, "*", num2, "=", multiply(num1, num2))
                elif basic_choice == 'd':
                    print(num1, "/", num2, "=", divide(num1, num2))
            else:
                print("Invalid Input")
        elif choice == '2':
            num1 = float(input("Enter base number: "))
            num2 = float(input("Enter exponent: "))
            print(num1, "^", num2, "=", power(num1, num2))
        elif choice == '3':
            num1 = float(input("Enter number: "))
            print("sqrt(", num1, ") =", sqrt(num1))
        elif choice == '4':
            num1 = float(input("Enter number: "))
            print("log(", num1, ") =", log(num1))
        elif choice == '5':
            print("Trigonometric Functions")
            print("a. Sine")
            print("b. Cosine")
            print("c. Tangent")
            trig_choice = input("Enter your choice (a/b/c): ")
            if trig_choice in ('a', 'b', 'c'):
                num1 = float(input("Enter angle in radians: "))
                if trig_choice == 'a':
                    print("sin(", num1, ") =", sin(num1))
                elif trig_choice == 'b':
                    print("cos(", num1, ") =", cos(num1))
                elif trig_choice == 'c':
                    print("tan(", num1, ") =", tan(num1))
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
