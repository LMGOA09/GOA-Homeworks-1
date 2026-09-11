#4)
# 'r' - "Read Mode": Opens an existing file to read data. Raises an error if the file does not exist.
# 'w' - "Write Mode": Opens a file to write data. Erases all existing content, or creates the file if it does not exist.
# 'a' - "Append Mode": Opens a file to add new data at the end without erasing existing content. Creates the file if it does not exist.
# 'b' - "Binary Mode": Tells Python to handle non-text files (like images or audio). Must be combined with r, w, or a.
# 'rb' - "Read Binary": Opens an existing non-text file to read binary data.
# 'wb' - "Write Binary": Opens a non-text file to write binary data, erasing any existing content.
# 'r+' - "Read & Write": Opens an existing file for both reading and modifying data.

#5)
# 'w' (Write): Deletes/wipes everything in the file immediately upon opening, then starts writing from scratch.
# 'a' (Append): Keeps existing content intact and adds all new text to the very end of the file.
# Both modes will automatically create a new file if the specified file does not exist yet.

#6)
total_students = int(input("Enter the number of students: "))

counter = 0

file = open("students.txt", "a")

while counter < total_students:
    name = input("Enter student name: ")
    has_homework = input("Has homework? (True/False): ")

    file.write("Name: " + name + " |: hasHomework: " + has_homework + "\n")

    counter = counter + 1

file.close()

print("Student records saved successfully!")