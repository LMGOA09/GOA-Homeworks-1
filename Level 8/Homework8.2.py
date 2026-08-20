#3) # Step 1: Get the target number from the user.
user_number = int(input("Enter a number: "))

# Step 2: Start our counter at 1.
counter = 1

# Step 3: Run the loop until the counter exceeds the user's number.
while counter <= user_number:
    
    # Step 4: Check if the number is even.
    # If a number divided by 2 has a remainder of 0, it is even.
    if counter % 2 == 0:
        print(counter, "this number is even.")
    else:
        # If there is a remainder (it will be 1), the number is odd.
        print(counter, "this number is odd.")
        
    # Step 5: Move to the next number.
    counter = counter + 1