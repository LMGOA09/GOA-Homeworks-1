#1)
import calculator

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))
num4 = float(input("Enter fourth number:"))

print("Addition result:", calculator.add(num1, num2))
print("Subtraction result:", calculator.subtract(num1, num2))
print("Multiplication result:", calculator.multiply(num1, num2))
print("Division result:", calculator.divide(num1, num2))

#2)
from person import get_age, get_name

name = get_name()
age = get_age()

print(f"Name: {name}")
print(f"Age: {age}")

#3)
import greetings

name = input("Enter a name: ")

greetings.hello(name)
greetings.goodbye(name)

#4)
import numbers

num = float(input("Enter a number: "))

print("Is the number even?", numbers.is_even(num))
print("Is the number positive?", numbers.is_positive(num))

#5)
from text_tools import lowercase, uppercase

user_text = input("Enter some text: ")

print("Uppercase:", uppercase(user_text))
print("Lowercase:", lowercase(user_text))

#6)
import multiplication

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result_multiply = multiplication.multiply(num1, num2)
result_square1 = multiplication.square(num1)
result_square2 = multiplication.square(num2)

print("Multiplication result:", result_multiply)
print(f"Square of {num1}:", result_square1)
print(f"Square of {num2}:", result_square2)

#7)
import student

print("Student name:", student.get_student_name())
print("Student score:", student.get_student_score())

#8)
from comparison import find_max, find_min

num1 = float("Enter first number: ")
num2 = float("Enter second number: ")

print("Largest number:", find_max(num1, num2))
print("Smallest number:", find_min(num1, num2))

#9)
import shop

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount percentage: "))

total_cost = shop.calculate_total(price, quantity)
discounted_price = shop.apply_discount(price, discount)

print("Total cost (without discount):", total_cost)
print("Price after discount (per item):", discounted_price)
print("Final total (with discounted unit price):", discounted_price * quantity)

#10)
import operations

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

print("Select operation:")
print("1. Division (a / b)")
print("2. Exponentiation (a ^ b)")

choice = input("Enter choice (1 or 2): ")
if choice == "1":
    result = operations.divide(num1, num2)
    print("Result:", result)
elif choice == "2":
    result = operations.power(num1, num2)
    print("Result:", result)
else:
    print("Invalid choice!")