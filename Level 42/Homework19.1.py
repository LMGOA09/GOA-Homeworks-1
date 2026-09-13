#4)
header = "hello world"
x = open("text.txt", "w")
x.write(header)
x.close()

#5)
def register(**kwargs):
    file = open("user_data.txt", "w")
    for key in kwargs:
        value = kwargs[key]
        file.write(key + ": " + value + "\n")
    file.close()

register(username="luka", email="user@mail.com", password="mysecretpassword")

#6)
def get_binary_file_size(filename):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    return len(data)

size = get_binary_file_size("text2.txt")
print(size)

#7)
def find_min_max(*args):
    largest = args[0]
    smallest = args[0]
    
    for num in args:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
            
    return largest, smallest

maximum, minimum = find_min_max(15, 3, 42, 8, 99, 2)
print("Largest:", maximum)
print("Smallest:", minimum)