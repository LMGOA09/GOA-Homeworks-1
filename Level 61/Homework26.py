#1)
day = int(input("Enter a number from 1 to 7: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

#2)
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    match op:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/":
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print(num1 / num2)
        case _:
            print("Invalid operation")


# We call the function to test it
calculator()

#3)
def calculate_sum(*args):
    total = sum(args)
    print("The sum is:", total)


calculate_sum(10, 20, 30, 40)

#4)
fruits = ["Apple", "Banana", "Orange"]

action = input("Enter an action (show, add, exit): ")

match action:
    case "show":
        print(fruits)
    case "add":
        new_fruit = input("Enter the new fruit: ")
        fruits.append(new_fruit)
        print("Updated list:", fruits)
    case "exit":
        print("Goodbye!")
    case _:
        print("Invalid choice")

#5)
def number_operations(*args):
    op = input("Enter an operation (sum, max, min): ")

    match op:
        case "sum":
            print("Sum:", sum(args))
        case "max":
            print("Max:", max(args))
        case "min":
            print("Min:", min(args))
        case _:
            print("Invalid choice")


# Example usage:
number_operations(5, 12, 3, 20, 8)