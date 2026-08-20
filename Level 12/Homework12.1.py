#4)
work_days = ("Monday", "Tuesday", "Wednesday", "Thursday")

# 1. Convert the tuple to a list
days_list = list(work_days)

# 2. Append the new element
days_list.append("Friday")

# 3. Convert it back to a tuple
work_days = tuple(days_list)

print(work_days)

#5)
colors = ("red", "green", "blue", "yellow")

tuple_length = len(colors)
print("The tuple has", tuple_length, "elements.")