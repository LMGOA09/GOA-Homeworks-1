#1)
squares = [x**2 for x in range (1, 21)]
print(squares)

#2)
evens = [x for x in range (1, 51) if x % 2 == 0]
print(evens)

#3)
odd_squares = [x**2 for x in range (1, 31) if x % 2 != 0]
print(odd_squares)

#4)
doubled = [x*2 for x in range (1, 16)]
print(doubled)

#5)
div_by_three = [x for x in range (1, 101) if x % 3 == 0]
print(div_by_three)

#6)
import random

random_numbers = [random.randint(1, 100) for _ in range (10)]
print(random_numbers)

#7)
import random

random_evens = []
for _ in range (15):
    num = random.randint(1, 50)
    if num % 2 == 0:
        random_evens.append(num)

#8)
import random

numbers = list(range(1, 21))
selected_number = numbers[random.randint(0, len(numbers) - 1)]

print("List:", numbers)
print("Selected number:", selected_number)

#9)
import time

start_time = time.time()

squares = [x**2 for x in range(1, 100001)]

end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")

#10)
import random

# Computer picks a random number between 1 and 10
secret_number = random.randint(1, 10)

# Get the user's guess
guess = int(input("Enter your guess (between 1 and 10): "))

# Check if the guess is correct
if guess == secret_number:
  print("Congratulations! You guessed the number!")
else:
  print("Unfortunately, you didn't guess it!")

print("The correct number was:", secret_number)