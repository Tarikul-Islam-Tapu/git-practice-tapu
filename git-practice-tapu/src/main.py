from datetime import date
from utils import add, subtract, multiply

print("Name: Tapu")
print(f"Today's Date: {date.today()}")

# Calculator functions
num1 = 10
num2 = 5

print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")