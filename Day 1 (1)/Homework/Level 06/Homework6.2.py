# 3) Create 2 lists, one for even numbers and one for odd numbers. Prompt the user to input 10 numbers, 
# and add the even numbers to the even numbers list and the odd numbers to the odd numbers list. 
# (Check for even/odd using n % 2 == 0)

even_numbers = []
odd_numbers = []
for i in range(10):
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)