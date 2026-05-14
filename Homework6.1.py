# 2) # Create an empty list, then prompt the user to input 5 numbers and use the .append() function to add all the numbers to this list.

list = []
numbers1 = int(input("Enter a number: "))
list.append(numbers1)
numbers2 = int(input("Enter a number: "))
list.append(numbers2)
numbers3 = int(input("Enter a number: "))
list.append(numbers3)
numbers4 = int(input("Enter a number: "))
list.append(numbers4)
numbers5 = int(input("Enter a number: "))
list.append(numbers5)
print(list)

print("Number of elements in the list:", len(list))