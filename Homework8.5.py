#5)
# CLI REGISTRATION AND AUTHORIZATION PROGRAM

# We will store registered users in a list of dictionaries.
# Each user will look like: {"username": "...", "email": "...", "password": "..."}
users_database = []

# This boolean variable controls our main program loop.
# As long as it is True, the menu keeps reappearing.
program_running = True

# Start the main loop using a 'while' statement
while program_running:
    # Display the Main Menu
    print("\n--- MAIN MENU ---")
    print("1. Registration")
    print("2. Login")
    print("3. Stop Program")
    
    # Get the user's menu choice
    choice = input("Choose an option (1-3): ")
    
    # --------------------------------------------------------------------------
    # OPTION 1: REGISTRATION
    # --------------------------------------------------------------------------
    if choice == "1":
        print("\n--- REGISTRATION ---")
        reg_username = input("Enter username: ")
        reg_email = input("Enter email: ")
        reg_password = input("Enter password: ")
        
        # Create a dictionary representing the new user
        new_user = {
            "username": reg_username,
            "email": reg_email,
            "password": reg_password
        }
        
        # Add the new user to our database list
        users_database.append(new_user)
        
        print("Registration success!")
        # Notice we do NOT change program_running, so it will automatically 
        # loop back to the main menu.

    # --------------------------------------------------------------------------
    # OPTION 2: LOGIN
    # --------------------------------------------------------------------------
    elif choice == "2":
        print("\n--- LOGIN ---")
        login_email = input("Enter your email: ")
        login_password = input("Enter your password: ")
        
        # We assume the credentials are wrong until we prove they are correct
        login_success = False
        
        # Use a counter loop or basic iteration to search through our database
        # We will loop through the index of the database list
        index = 0
        while index < len(users_database):
            # Fetch the user at the current index
            current_user = users_database[index]
            
            # Check if both email and password match
            if current_user["email"] == login_email and current_user["password"] == login_password:
                login_success = True
                # Break out of this internal loop early since we found the user
                break
                
            index = index + 1
            
        # Check the results of our search
        if login_success:
            print("Login success!")
            # The instructions state: "if the information is correct... close the program."
            # We set program_running to False so the outer while loop terminates.
            program_running = False
        else:
            print("Error: Invalid email or password. Returning to main menu.")

    # --------------------------------------------------------------------------
    # OPTION 3: STOP PROGRAM
    # --------------------------------------------------------------------------
    elif choice == "3":
        print("Stopping program. Shutting Down!")
        # Break the main loop to close the program
        program_running = False

    # --------------------------------------------------------------------------
    # INVALID OPTION HANDLING
    # --------------------------------------------------------------------------
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

# The program naturally ends here once the while loop finishes.