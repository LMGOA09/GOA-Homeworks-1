### 3) Explain if-elif-else
# 'if' starts the check. If the condition is true, the code inside runs.
# 'elif' (short for else-if) checks a new condition ONLY if the previous ones were false.
# 'else' is the "catch-all" that runs if none of the conditions above it were true.

### 4) Explain and-or
# 'and' requires BOTH conditions to be true to run the code.
# 'or' requires ONLY ONE of the conditions to be true to run the code.

# ---------------------------------------------------------
# 1) Odd or Even
num1 = int(input("Enter a number to check if it is odd or even: "))
if num1 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# ---------------------------------------------------------
# 2) Traffic Light System
light = input("Enter light color (green/yellow/red): ")
if light == "green":
    print("go")
elif light == "yellow":
    print("get ready")
else:
    print("stop")

# ---------------------------------------------------------
# 5) Positive Number Check
print("Checking two numbers:")
val1 = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))

if val1 > 0 and val2 > 0:
    print("Both are positive")
elif val1 > 0 or val2 > 0:
    print("Only one is positive")
else:
    print("None are positive")

# ---------------------------------------------------------
# 6) Check if equal to 10
ten_check = int(input("Enter a number to check against 10: "))
if ten_check == 10:
    print("The number is equal to 10")
else:
    print("The number is not equal to 10")

# ---------------------------------------------------------
# 7) Discounts (Age and Student Card)
age_discount = int(input("Enter your age: "))
has_card = input("Do you have a student card? (yes/no): ")

if age_discount < 18 or has_card == "yes":
    print("You have savings!")
elif age_discount >= 60 and has_card == "no":
    print("You have a senior discount!")
else:
    print("You are not eligible for the discount")

# ---------------------------------------------------------
# 8) Divisibility Check
n = int(input("Enter the main number: "))
d = int(input("Enter the divisor: "))
if n % d == 0:
    print("The number is divisible")
else:
    print("The number is not divisible")

# ---------------------------------------------------------
# 9) Heart Rate Advice
user_age = int(input("Enter your age for heart rate check: "))
hr = int(input("Enter your heart rate: "))

if user_age < 30 and hr < 140:
    print("You can exercise more")
elif user_age >= 30 and hr > 170:
    print("You need to rest")
else:
    print("Activity level is normal")

# ---------------------------------------------------------
# 10) Estimating Weight by Age
w_age = int(input("Enter age for weight check: "))
w_weight = int(input("Enter weight: "))

if w_age < 10:
    if w_weight < 20:
        print("Weight is low")
    elif w_weight >= 20 and w_weight <= 40:
        print("Weight is normal")
    else:
        print("Weight is high")

elif w_age >= 10 and w_age <= 17:
    if w_weight < 40:
        print("Underweight")
    elif w_weight >= 40 and w_weight <= 65:
        print("Normal weight")
    else:
        print("Overweight")

else: # 18 or older
    if w_weight < 50:
        print("Underweight")
    elif w_weight >= 50 and w_weight <= 90:
        print("Normal weight")
    else:
        print("Overweight")