#1)
# WHAT IS A WHILE LOOP?
# A 'while' loop is a control flow statement that allows code to be executed 
# repeatedly based on a given Boolean condition. You can think of it as a 
# repeated 'if' statement. If the condition is True, the code inside runs. 
# Once it finishes, it checks the condition again. This repeats until the 
# condition becomes False.

# HOW IS IT WRITTEN?
# In Python, it follows this structure:
# while condition:
#     # code to execute while condition is true
#     # increment or change the variable affecting the condition

# WHAT IS IT USED FOR?
# 1. When you don't know in advance how many times the loop needs to run 
#    (e.g., waiting for a user to type 'exit').
# 2. Reading data until the end of a file is reached.
# 3. Creating game loops or menu loops that run continuously.

# CRITICAL WARNING: THE "INFINITE LOOP"
# If the loop's condition never becomes False, the loop will run forever, 
# freezing your program. You must always ensure that something inside the 
# loop changes the condition (like increasing a counter variable).