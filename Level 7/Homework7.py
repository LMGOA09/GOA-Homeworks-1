#1 Create a program that prints the numbers 1 to 20 using a "for" loop.
for i in range(1, 21):
    print(i)

#2 Have the user input a number using the int() function and print all the numbers from 1 to that number using a for loop.
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    print(i)

#3 Create a list with 5 names and print each name separately using a for loop.
names = ["Luka Motiashvili", "Ucha Tabatadze", "Beqa Abuladze", "Mate Gzirishvili", "Saba Grigalashvili"]
for name in names:
    print(name)

#4 Create an empty list. Have the user input a word 5 times using a for loop and add each to the list using the append() function. 
# Finally, print all the elements using a for loop.
words = []
for i in range(5):
    word = input("Enter a word: ")
    words.append(word)

print("Your words are:")
for word in words:
    print(word)

#5 Create a list of numbers. Find the sum of all the numbers using a for loop.
numbers = [10, 20, 30, 40, 50]
total_sum = 0

for num in numbers:
    total_sum = total_sum + num

print("The sum is:", total_sum)