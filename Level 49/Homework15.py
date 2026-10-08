#1)
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

try:
    age = int(input("Enter your age: "))
except ValueError:
    age = "Invalid age entered"

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
except ValueError:
    result = "Error: Please enter valid numbers"
except ZeroDivisionError:
    result = "Error: Cannot divide by zero"

print("\n--- User Summary ---")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Division Result: {result}")

#2)
# *args: Allows a function to take any number of positional arguments as a tuple;
# **kwargs: Allows a function to take any number of keyword (named) arguments as a dictionary.

# *args demo:
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(5, 10, 15))

# **kwargs demo:
def show_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_user_info(name="Luka", role="Developer")