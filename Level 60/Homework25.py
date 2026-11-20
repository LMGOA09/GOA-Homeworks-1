#1)
def calculate_product(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(calculate_product(2, 3, 4))

#2)
def configure_car(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} -> {value}")


configure_car(brand="Alfa Romeo", model="Giulia Ti Q4", year=2022, color="White")

#3)
import random

pin = random.randint(1000, 9999)
print("Your PIN:", pin)

#4)
import time

for i in range(5, 0, -1):
    print(i)
    time.sleep(1) # .sleep() is a "delayer" for 1 second.

print("Time's up!")

#5)
odd_numbers = [x for x in range(1, 41) if x % 2 != 0]

print(odd_numbers)

#6)
cubes = [x**3 for x in range(1, 13)]

print(cubes)

#7)
words = ["მანქანა", "ვაშლი", "მზე", "სახლი", "მდინარე"]

m_words = [word for word in words if word.startswith("მ")]

print(m_words)

#8)
numbers = [-3, 5, -1, 0, 8, -10, 4]

result = [x if x >= 0 else 0 for x in numbers]

print(result)