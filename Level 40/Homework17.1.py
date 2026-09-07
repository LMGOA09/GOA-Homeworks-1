#5)
learners_python = {"nino", "giorgi", "ana", "levani", "mariami"}
learners_javascript = {"giorgi", "ana", "david", "sofo", "levani"}

# intersection - learners studying both languages:
both = learners_python & learners_javascript
print("Both languages:", both)

# difference - learners studying Python only:
only_python = learners_python - learners_javascript
print("Only Python:", only_python)

# difference - learners studying JavaScript only:
only_javascript = learners_javascript - learners_python
print("Only Javascript:", only_javascript)

# union - learners from both languages:
all_learners = learners_python | learners_javascript
print("All learners:", all_learners)

# symmetric difference - learners studying only one language:
only_one = learners_python ^ learners_javascript
print("Only one language:", only_one)

#6)
# creating an empty set:
numbers = set()

# adding numbers 10-50 using .update:
numbers.update([10, 20, 30, 40, 50])

# adding another list containing 30, 60, 70:
numbers.update([30, 60, 70])

# removing 20 from the list:
numbers.discard(20)

# removing a random element:
removed_item = numbers.pop()
print(f"Randomly removed item: {removed_item}")

# final result:
print("Final set:", numbers)
print("Length of final set:", len(numbers))