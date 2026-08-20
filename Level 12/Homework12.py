#1)
fruits = ("apple", "banana", "peach", "strawberry")

if "peach" in fruits:
    print("Yes, peach is in the fruits tuple!")
else:
    print("No, peach was not found.")

#2)
numbers = (5, 12, 8, 24, 3, 17)

first_element = numbers[0]
last_element = numbers[-1]

print("First element:", first_element)
print("Last element:", last_element)

#3)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined_tuple = tuple1 + tuple2
print(combined_tuple)