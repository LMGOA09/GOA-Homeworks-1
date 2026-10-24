#1)
def sum_all(*args): # Reminder: accepts any number of normal values (like 316, 337, 381...); also groups values into a Tuple.
    return sum(*args)

#2)
def print_student_info(**kwargs): # Reminder: accepts named values (like name="Qaikhosro", age=30); also groups values into a Dictionary.
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

#3)
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Nope, I refuse to divide by zero because it's prohibited! :(")
except ValueError:
    print("Invalid characters used! (Please enter numbers only.)")

#4)
try:
    file = open("my_note_here.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    print(file.read())
    file.close()
finally:
    print("Program finished! Nicely done.")

#5)
f = open("my_note_here2.txt", "w")
f.write("Line 1\n")
f.close()

#6)
file = open("my_note_here3.txt", "rb")
data = file.read(10)
print(data)

file.close()