#1)
# Square brackets raise a KeyError if the key is missing.
# .get() returns None (or a specified default value) without raising an error.

data = {"a": 1}
print(data["a"])
print(data.get("a"))

print(data["b"])
print(data.get("b"))

#2)
# dict(a="val1") creates a dictionary directly from keyword arguments (keys are strings).
# dict.fromkeys(iterable, value) creates a dictionary using elements of an iterable as keys, all mapping to the same initial value.

# dict.fromkeys([1, 2, 3], "test") creates:
# {1: 'test', 2: 'test', 3: 'test'}

#3)
countries = {"Spain": "Madrid", "Germany": "Berlin"}

countries["Italy"] = "Rome"
countries["Germany"] = "Munich"

print(countries)

#4)
scores = {"Python": 90, "JavaScript": 85, "HTML + CSS": 88}

kotlin_score = scores.get("Kotlin", "Kotlin score not specified")
print(kotlin_score)

#5)
club_cities = {"georgia": "tbilisi", "manchester": "united", "london": "chelsea"}
del club_cities["manchester"]
print(club_cities)

#6)
ids = [101, 102, 103, 104]
status_dict = dict.fromkeys(ids, "Pending")
print(status_dict)

#7)
cars = dict(alfa="giulia q4", alfa="stelvio q4", alfa="giulietta jtd")
print(cars)