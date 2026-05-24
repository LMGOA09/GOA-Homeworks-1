#2)
# Step 1: Get input from the user. 
# We use int() because input() reads everything as text (strings), and we need a number.
user_number = int(input("Enter a number: "))

# Step 2: Initialize a counter variable at 1.
# This keeps track of our current position.
counter = 1

# Step 3: Start the while loop.
# The loop will keep running as long as the counter is less than or equal to the user's number.
while counter <= user_number:
    # Print the current value of the counter.
    # (Per requirements, we are not using f-strings, so we use commas to separate)
    print(counter)
    
    # Step 4: Increment the counter by 1.
    # Crucial step! Without this, counter stays 1 forever, causing an infinite loop.
    counter = counter + 1