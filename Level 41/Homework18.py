#1)
# Before:
# x=open(“text.txt”,”w”)
# x.write(“Hello World”)
# print(x.read())

# After:
x = open("text.txt", "w") 
x.write("Hello World")
x.close() 

x = open("text.txt", "r")
print(x.read())
x.close() # This is necessary because of demonstrating the results

#2)
file = open("todo.txt", "a")

task1 = input("Enter first task: ")
file.write(task1 + "\n")

task2 = input("Enter second task: ")
file.write(task2 + "\n")

task3 = input("Enter third task: ")
file.write(task3 + "\n")

file.close()

print("All tasks saved successfully!")

#3)
def log_user_activity(username, action):
    file = open("activity.log", "a")

    log_line = "User: " + username + " |: Action: " + action + "\n"

    file.write(log_line)

    file.close()

# Example:
log_user_activity("Luka", "Logged In")
log_user_activity("Luka", "Edited Profile")