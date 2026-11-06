#15)
emails = [
    "grigolkhandzteli81@gmail.com",
    "egnateninoshvili44@yahoo.com",
    "arnoldchiqobava27gmail.com",
    "simonkandelaki53@gmail.com",
    "petreqavtaradze70@outlook.com",
    "akakitsereteli77@gmail"
]

valid_emails = list(filter(lambda e: "@" in e and e.endswith(".com"), emails))
print(valid_emails)

#9)
numbers = [306, 314, 326, 337, 346, 351, 364, 370, 381, 392]

result = list(filter(lambda n: n > 20 and n % 5 == 0, numbers))
print(result)

#10)
prog_students = [
    {"name": "Gia_Chanturia", "grade": 86},
    {"name": "Givi_Kartozia", "grade": 52},
    {"name": "Ioane_Petritsi", "grade": 95},
    {"name": "Rafael_Agladze", "grade": 74},
    {"name": "Petre_Iberi", "grade": 49},
    {"name": "Bogdan_Khmelnitski", "grade": 31}
]

top_prog_students = list(filter(lambda s: s["grade"] > 70, prog_students))
print(top_prog_students)

#11)
words = ["apple", "banana", "kiwi", "strawberry", "pear", "watermelon"]

result = list(filter(lambda w: "a" in w and len(w) >= 5, words))
print(result)

#12)
users = [
    {"name": "Alexandre_Managadze", "age": 16, "active": True},
    {"name": "Gigo_Zaziashvili", "age": 22, "active": False},
    {"name": "David_Sarajishvili", "age": 19, "active": True},
    {"name": "Kote_Marjanishvili", "age": 25, "active": True},
    {"name": "Alio_Mirtskhulava", "age": 21, "active": False},
    {"name": "Elefter_Andronikashvili", "age": 18, "active": False}
]

active_adults = list(filter(lambda u: u["age"] >= 18 and u["active"], users))
print(active_adults)

#13)
products = [
    {"name": "Phone", "price": 1000},
    {"name": "Laptop", "price": 2500},
    {"name": "Mouse", "price": 50},
    {"name": "Monitor", "price": 700},
    {"name": "Keyboard", "price": 120}
]

affordable = list(filter(lambda p: 100 <= p["price"] <= 1000, products))
print(affordable)

#14)
numbers = [121, 144, 169, 200, 225, 256, 300, 324]

result = list(filter(lambda n: (n ** 0.5).is_integer(), numbers))
print(result)