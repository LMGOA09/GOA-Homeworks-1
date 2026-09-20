#1)
# "try" runs a code directly without permission (it crashes anyway, equivalent to a video game running with thousand bugs);
# "except" is for this scenario: If it crashes with a specific error, it catches it and runs the recovery code here;
# "else" runs this code only if the "try" block succeeded with zero errors;
# "finally" runs the code all the way at the end, no matter what (Ideal for a cleanup procedure).

# Demo:
try:
    num = int(input("Enter a number here: "))
    result = 100 / num
except ValueError:
    print("Heeeey, that's not a valid number!")
except ZeroDivisionError:
    print("Nope, I don't have a right to divide by zero!")
else:
    print(f"Math worked as expected! Result is: {result}")
finally:
    print("Attempt finished, well done.")

#2)
def get_char(text, position):
    try:
        char = text[position]
    except IndexError:
        print("Heeeey, this position doesn't exist in the text!")
    else:
        print("Character successfully retrieved! Well done.")
        return char

#3)
colors = {"red", "green", "blue"}

try:
    color = input("Enter a color to remove: ")
    color.remove(color)
except KeyError:
    print("Heeeey, this color is not in the set!")
finally:
    print("Operation completed! Well done.")