# Note: these comments in every objective here are brief reminders during explanation procedures.

#1)
numbers = [1, 2, 3, 4, 5]

doubled_numbers = list(map(lambda x: x * 2, numbers))

for num in doubled_numbers:
    print(num)

# map() takes two things: a function and a list.
# It applies the function to EVERY single item in the list automatically.
# lambda: A keyword that makes a quick, temporary function (without needing 'def').

#2)
numbers = [2, 4, 6, 8, 10]

squared_numbers = list(map(lambda x: x ** 2, numbers))

for num in squared_numbers:
    print(num)

# ** means "to the power of" (exponent). 
# Here, lambda x: x ** 2 squares each number in the list.

#3)
names = ["Lukson", "Nikoloz", "Sabunor", "Giorgi"]

upper_names = list(map(lambda name: name.upper(), names))

for name in upper_names:
    print(name)

#4)
prices = [10, 20, 30, 40, 50]

new_prices = list(map(lambda price: price + 10, prices))

for price in new_prices:
    print(price)

#5)
numbers = [100, 200, 300, 400, 500]

reduced_numbers = list(map(lambda x: x - 50, numbers))

for num in reduced_numbers:
    print(num)