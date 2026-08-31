#1)
capitals = {
    "Georgia": "Tbilisi",
    "France": "Paris",
    "Japan": "Tokyo",
    "Italy": "Rome"
}

for country in capitals.keys():
    print(country)

#2)
students_scores = {
    "Nikoloz": 90,
    "Ana": 85,
    "Giorgi": 95
}

for name in students_scores:
    score = students_scores[name]
    print(f"Student {name} received {score} points.")

#3)
user_profile = {"name": "Luka", "age": 20}

#1. Adding "Georgia" as value:
user_profile.setdefault("country", "Georgia")

#2. Changing "age" to 25 via setdefault
user_profile.setdefault("age", 25)

print(user_profile)

#4)
fruit_prices = {
    "Apple": 3.50,
    "Banana": 4.20,
    "Orange": 2.80,
    "Peach": 5.00
}

for fruit, price in fruit_prices.items():
    print(f"{fruit} : {price} GEL")