import sys
import os
import math 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def rest_div(x, y):
    return x % y

def power(x, y):
    return x ** y

def square_root(x):
    return x ** 0.5

def logarithm(x):
    return math.log(x)

def logarithm_generalised(x, y):
    return math.log(x, y)

def exponential(x):
    return math.exp(x)

def factorial(x):
    return math.factorial(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))    

def tangent(x):
    return math.tan(math.radians(x))

def cotangent(x):
    return 1 / math.tan(math.radians(x))

def percentage1(x, y):
    return (x/y)*100
    
def percentage2(x, y):
    return (x/100)*y


print("Select operation:")
print("Add(+)")
print("Subtract(-)")
print("Multiply(*)")
print("Divide(/)")
print("Rest of division(%)")
print("Power(^)")
print("Square root(sqrt)")
print("Logarithm(a base b)(log)")
print("Natural Logarithm(ln)")
print("Exponential(exp)")
print("Factorial(!)")
print("Sine(sin)")
print("Cosine(cos)")
print("Tangent(tan)")
print("Cotangent(cot)")
print("Exit")
print("Percentage(a from b)(%1)")
print("Percentage(a percent of b)(%2)")


while True:
    num1 = float(input("Enter first number: "))
    choice = input("Enter choice: ")
    if choice == '15':
        print("Exiting...")
        sys.exit()
    
    if choice in ('+', '-', '*', '/', '%', '^', '%1', '%2', 'log'):
        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '%':
            print(int(num1), "%", int(num2), "=", int (divide (num1, num2)), "rest", rest_div(num1, num2))
        
        elif choice == '^':
            print(num1, "^", num2, "=", power(num1, num2))

        elif choice == '%1':
            print(num1, "%->", num2, "=", percentage1(num1, num2))

        elif choice == '%2':
            print(num1, "%", " of", num2, "=", percentage2(num1, num2))
        
        elif choice == 'log':
            print("log", num1, "base", num2, "=", logarithm_generalised(num1, num2))
          
    if choice in ('sqrt', 'ln', 'exp', '!', 'sin', 'cos', 'tan', 'cot'):

        if choice == 'sqrt':
            print(num1, "^ 0.5", "=", square_root(num1))
        
        elif choice == 'ln':
            print("ln", num1, "=", logarithm(num1))
        
        elif choice == 'exp':
            print("exp", num1, "=", exponential(num1))

        elif choice == '!':
            print(num1, "!", "=", factorial(int(num1)))
        
        elif choice == 'sin':
            print("sin", num1, "=", sine(num1))
        
        elif choice == 'cos':
            print("cos", num1, "=", cosine(num1))

        elif choice == 'tan':
            print("tan", num1, "=", tangent(num1))

        elif choice == 'cot':
            print("cot", num1, "=", cotangent(num1))
    
    next_calculation = input("Continue? (yes/no): ")
    if next_calculation == "no":
        sys.exit()
else:
    print("Invalid input. Please enter a number from 1 to 18.")

    
    