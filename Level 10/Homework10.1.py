# 2) FUNCTION: minimum

def minimum(arr):
    """
    Finds and returns the smallest number in a given array.
    Assumes the array is not empty.
    """
    # Start by assuming the first number is the smallest
    lowest = arr[0]
    
    # Loop through the rest of the array
    for num in arr:
        # If we find a number smaller than our current lowest, update it
        if num < lowest:
            lowest = num
            
    return lowest

# 3) FUNCTION: maximum
def maximum(arr):
    """
    Finds and returns the largest number in a given array.
    Assumes the array is not empty.
    """
    # Start by assuming the first number is the largest
    highest = arr[0]
    
    # Loop through the rest of the array
    for num in arr:
        # If we find a number larger than our current highest, update it
        if num > highest:
            highest = num
            
    return highest

# 4) FUNCTION: sum_manual
def sum_manual(arr):
    """
    Calculates and returns the total sum of all numbers in an array.
    """
    # Initialize a counter variable at 0
    total = 0
    
    # Add each number in the array to our total
    for num in arr:
        total += num
        
    return total

# 5) FUNCTION: even_or_odd
def even_or_odd(number):
    """
    Checks if a number is even or odd using the modulo (%) operator.
    """
    # If a number divided by 2 leaves a remainder of 0, it's even
    if number % 2 == 0:
        return "This number is even"
    else:
        return "This number is odd"


# OPTIONAL: TESTING THE FUNCTIONS

# You can uncomment the lines below to test how these functions work!

# sample_array = [12, 5, 8, 23, -3, 17]
# print("Smallest number:", minimum(sample_array))   # Expected: -3
# print("Largest number:", maximum(sample_array))     # Expected: 23
# print("Sum of numbers:", sum_manual(sample_array))  # Expected: 62
# print(even_or_odd(7))                               # Expected: This number is odd
# print(even_or_odd(14))                              # Expected: This number is even