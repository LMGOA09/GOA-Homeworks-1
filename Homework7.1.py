#6 Have the user input a number 5 times using a for loop, add them to the list, and finally print each element and the 
# length of the list using the len() function.
import numbers

num_list = []
for i in range(5):
    num = int(input("Enter a number: "))
    num_list.append(num)

print("Elements in the list:")
for n in num_list:
    print(n)

print("Length of the list is:", len(num_list))

#7 Create a list: ["apple", "banana", "orange", "kiwi"]. Use a for loop to find "banana" and remove it with the remove() function, 
# then use a for loop to print the remaining elements.
fruits = ["apple", "banana", "orange", "kiwi"]

for fruit in fruits:
    if fruit == "banana":
        fruits.remove("banana")

print("Remaining fruits:")
for fruit in fruits:
    print(fruit)

#8 Have the user enter a number and use a for loop to print the multiplication table of that number from 1 to 10.
num = int(input("Enter a number for the multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#9 Create a list of 10 numbers and use a for loop to print only the even numbers.
numbers = [12, 7, 22, 15, 40, 3, 18, 9, 50, 6]
print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)

#10 Create a program that asks the user to enter a name 5 times using a for loop, adds it to the list, and then 
# prints all the names using a for loop.
name_list = []
for i in range(5):
    name = input("Enter a name: ")
    name_list.append(name)

print("All names:")
for name in name_list:
    print(name)