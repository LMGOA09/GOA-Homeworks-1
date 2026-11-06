#1)
prices = [120, 250, 80, 450, 600, 35, 900]

new_prices = list(map(lambda p: round(p * 1.18, 2), prices))
print(new_prices)

#2)
academy_grades = [45, 67, 89, 32, 100, 76, 54]

new_academy_grades = list(map(lambda g: min(g + 7, 100), academy_grades))
print(new_academy_grades)

#3)
words = ["python", "javascript", "html", "css", "react"]

result = list(map(lambda w: f"{w.upper()} - {len(w)} letters", words))
for item in result:
    print(item)

#4)
numbers = [12, 25, 34, 47, 56, 63, 78]

result = list(map(lambda n: (n * 3 + 10) / 2, numbers))
print(result)

#5)
users = [
    {"name": "Iona_Meunargia", "age": 16},
    {"name": "Nikoloz_Khudadovi", "age": 21},
    {"name": "Iotam_Zedginidze", "age": 19},
    {"name": "Ioane_Zosime", "age": 25},
    {"name": "Pavle_Ingorokva", "age": 27},
    {"name": "Aleko_Gobronidze", "age": 17}
]

result = list(map(lambda u: f"{u['name']} is {u['age']} years old.", users))
for item in result:
    print(item)

#6)
temperatures = [0, 10, 20, 30, 40, 100]

fahrenheit = list(map(lambda c: c * 1.8 + 32, temperatures))
print(fahrenheit)

#7)
words = ["program", "system", "memory", "files", "code"]

result = list(map(lambda w: len(w) * 2, words))
print(result)

#8)
products = [
    {"name": "Galaxy Buds", "price": 500},
    {"name": "Galaxy Watch", "price": 900},
    {"name": "Galaxy Book", "price": 3500}
]

updated_products = list(map(lambda p: {"name": p["name"], "price": p["price"] * 1.15}, products))
print(updated_products)