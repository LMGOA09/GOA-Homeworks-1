#1)
# Fixed Code:
name = "Saba"  # Error: Missing closing quotation mark (")
age = 16       # Error: '!=' is a comparison; use '=' for assignment. Also removed quotes to keep it an integer.
number1 = 10
number2 = 10   # Error: '->' is not a valid assignment operator; use '='. Removed quotes to allow math.

print(name)    # Error: print("name") would just print the word "name", not the variable value.
print(age)     # Error: Removed quotes to print the variable value.
print(number1 + number2) # Error: Variables are case-sensitive (number1 vs NUMBER1). Added missing ')'.