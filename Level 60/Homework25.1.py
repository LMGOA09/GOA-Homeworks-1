#9)
languages = ["python", "javascript", "html", "css", "c++"]

lengths = [len(lang) for lang in languages]

print(lengths)

#10)
multiples_of_11 = [x for x in range(1, 101) if x % 11 == 0]

print(multiples_of_11)

#11)
words = ["frontend", "backend", "fullstack", "database"]

uppercase_words = [word.upper() for word in words]

print(uppercase_words)

#12)
# We have numbers from 1 to 50 divisible by 2 but, by 4
result = [x for x in range(1, 51) if x % 2 == 0 and x % 4 != 0]

print(result)

#13)
# We replace even numbers with "Even" and odd with "Odd" for numbers 1 to 15
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 16)]

print(labels)

#14)
matrix = [[10, 20], [30, 40], [50, 60]]

# We flatten the 2D list into 1D
flat_list = [num for row in matrix for num in row]

print(flat_list)