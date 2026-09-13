#1)
# rb (Read Binary): Opens a file for reading in raw binary format (bytes) instead of normal text;
# wb (Write Binary): Opens a file for writing in raw binary format. It creates a new file or overwrites an existing file.,

# Demonstrational bits:
file = open("data.bin", "wb")
file.write(b"Hello World")
file.close()

file = open("data.bin", "rb")
content = file.read()
file.close()

print(content)

# #2)
# *args: Allows a function to accept any number of positional arguments as a tuple;
# **kwargs: Allows a function to accept any number of keyword arguments (key-value pairs) as a dictionary.

# Demonstrational bits:
def show_args(*args):
    print(args)

show_args("python", "javascript", "html")

def show_kwargs(**kwargs):
    print(kwargs)

show_kwargs(username="luka", email="test@mail.com")

#3)
def join_words(*args):
    result = ""
    index = 0
    for word in args:
        if index == 0:
            result = result + word
        else:
            result = result + "-" + word
        index = index + 1
    return result

print(join_words("python", "javascript", "html"))
