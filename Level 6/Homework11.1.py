#4)
# Create an empty set
loop_set = set()

# Loop from 1 to 20
for i in range(1, 21):
    loop_set.add(i)

print(loop_set)

#5)
# Create an empty set
odd_set = set()

# Loop through a range of numbers (e.g., 1 to 20)
for i in range(1, 21):
    if i % 2 != 0:  # Checks if the number is odd
        odd_set.add(i)

print(odd_set)

#6)
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_b = {"python", "hello", "world"}

# Combine them using union
combined_set = set_a.union(set_b)

print(combined_set)

#7)
# Create an empty set
final_set = set()

# Create a list (often referred to as an array in general programming)
my_array = [10, 20, 30, 40, 50]

# Use update to add the elements of the array to the set
final_set.update(my_array)

print(final_set)