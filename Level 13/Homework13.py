#1)
def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

#2)
def sum_array(numbers):
    return sum(numbers)

#3)
def positive_sum(numbers):
    return sum(num for num in numbers if num > 0)