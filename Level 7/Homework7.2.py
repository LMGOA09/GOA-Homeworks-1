#11 Create a list of 5 numbers. Use a for loop to find the largest number.

numbers = [15, 42, 7, 89, 23]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)

#12 Have the user enter a word and use a for loop to print each letter of that word separately.
word = input("Enter a word: ")
for letter in word:
    print(letter)

#13 Create a list of animal names. Use a for loop to iterate through the list and print the name of each animal in uppercase.
animals = ["lion", "tiger", "elephant", "zebra"]
for animal in animals:
    print(animal.upper())

#14 Create a program where the user enters how many numbers to add to a list. Use a for loop to enter the number that many times, 
# add it with the append() function, and finally use a for loop to print all the elements and the len() function to print the length of the list.
count = int(input("How many numbers do you want to add? "))
user_numbers = []

for i in range(count):
    num = int(input("Enter a number: "))
    user_numbers.append(num)

print("Your elements:")
for num in user_numbers:
    print(num)

print("Total count of elements:", len(user_numbers))

#15 Create a list of numbers. Use a for loop to count how many positive and how many negative numbers are in the list.
numbers = [10, -5, 3, -1, 0, 7, -8]
pos_count = 0
neg_count = 0

for num in numbers:
    if num > 0:
        pos_count = pos_count + 1
    elif num < 0:
        neg_count = neg_count + 1

print("Positive numbers:", pos_count)
print("Negative numbers:", neg_count)