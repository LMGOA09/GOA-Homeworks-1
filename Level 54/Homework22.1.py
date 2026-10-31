#6)
words = ["apple", "banana", "cat", "computer", "dog"]

word_lengths = list(map(len, words))

for length in word_lengths:
    print(length)

#7)
temperatures = [0, 10, 20, 30, 40]

fahrenheit_temps = list(map(lambda c: c * 1.8 + 32, temperatures))

for temp in fahrenheit_temps:
    print(temp)

#8)
numbers = [30, 60, 90, 120, 150]

divided_numbers = list(map(lambda x: x / 3, numbers))

for num in divided_numbers:
    print(num)

#9)
ages = [12, 15, 16, 14, 17]

new_ages = list(map(lambda age: age + 1, ages))

for age in new_ages:
    print(age)

#10)
numbers = [5, 10, 15, 20, 25, 30]

multiplied_numbers = list(map(lambda x: x * 4, numbers))

for num in multiplied_numbers:
    if num > 50:
        print("greater than 50")
    else:
        print("less than or equal to 50")