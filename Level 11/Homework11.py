#1)
# Create an empty set
my_set = set()

# Add 5 elements
my_set.add("Apple")
my_set.add("Banana")
my_set.add("Cherry")
my_set.add(42)
my_set.add(7)

print(my_set)

#2)
# Create the initial set
mixed_set = {1, 2, 3, 4, 5, 5, 5, 6, 7, "python"}

# Add "hello"
mixed_set.add("hello")

# Remove "python"
mixed_set.remove("python")

print(mixed_set)

#3)
# Create the set from 1 to 10
num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Create an empty list
even_list = []

# Loop through the set and add even numbers to the list
for num in num_set:
    if num % 2 == 0:
        even_list.append(num)

print(even_list)