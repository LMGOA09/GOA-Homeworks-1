#18)
products = ["Phone", "Laptop", "Mouse", "Keyboard"]
prices = [1000, 2500, 50, 120]
quantities = [2, 1, 5, 3]

grand_total = 0
for product, price, qty in zip(products, prices, quantities):
    total_cost = price * qty
    grand_total += total_cost
    print(f"{product} total cost: {total_cost}")

print(f"Grand Total: {grand_total}")

#19)
prog_students = ["Valentin_Topuridze", "Vaso_Godziashvili", "Romanoz_Khomleli", "Mikheil_Gakhokidze"]
javascript = [90, 75, 85, 60]
python = [85, 95, 70, 80]

for student, m_score, p_score in zip(prog_students, javascript, python):
    avg = (m_score + p_score) / 2
    print(f"{student}'s average score: {avg}")

#20)
team_a = [85, 90, 75, 100, 65]
team_b = [80, 95, 70, 90, 85]

for i, (score_a, score_b) in zip(team_a, team_b):
    if score_a > score_b:
        print(f"Round {i}: Team A wins")
    elif score_b > score_a:
        print(f"Round {i}: Team B wins")
    else:
        print(f"Round {i}: It's a tie")

#21)
names = ["Omar_Khizanishvili", "Ilia_Chavchavadze", "Besarion_Zghenti", "Zhiuli_Shartava"]
ages = [16, 20, 17, 23]
cities = ["Tbilisi", "Akhaltsikhe", "Borjomi", "Mtskheta"]

for name, age, city in zip(names, ages, cities):
    if age == 18:
        print(f"{name} is 18 years old and lives in {city}.")

#22)
numbers = [5, 12, 18, 23, 30, 7, 40, 55, 60]

result = map(lambda x: x * 2, filter(lambda x: x > 15, numbers))

new_numbers = list(result)
print(new_numbers)

#23)
names = ["Jano_Bagrationi", "Tengiz_Sheshelidze", "Akaki_Vasadze", "Vladimer_Lobzhanidze", "Iason_Lortqipanidze"]
ages = [16, 22, 25, 17, 20]

# Combine names and ages
combined = zip(names, ages)

# Keep only those who are >= 18
adults = filter(lambda person: person[1] >= 18, combined)

# Format into strings using map
formatted = map(lambda person: f"{person[0]} is {person[1]} years old", adults)

print(list(formatted))

#24)
products = [
    {"name": "Phone", "price": 1000, "quantity": 5},
    {"name": "Laptop", "price": 2500, "quantity": 2},
    {"name": "Mouse", "price": 50, "quantity": 20},
    {"name": "Monitor", "price": 700, "quantity": 0},
    {"name": "Keyboard", "price": 120, "quantity": 10},
]

# Keep only products with quantity > 0
available_products = filter(lambda p: p["quantity"] > 0, products)


# Calculate total value and print name + total value
def get_total(p):
  total_value = p["price"] * p["quantity"]
  print(f"{p['name']} - Total Value: {total_value}")
  return total_value


list(map(get_total, available_products))

#25)
names = ["Dimitri_Gulia", "Tbel_Abuseridze", "Paata_Datuashvili", "Akaki_Kvantaliani", "Gia_Romelashvili"]
javascript_grades = [90, 65, 80, 45, 95]
python_grades = [85, 75, 90, 55, 100]

students = zip(names, javascript_grades, python_grades)

# Calculate average and filter for average > 70
smart_students = filter(
    lambda s: (s[1] + s[2]) / 2 > 70, students
)

# Create formatted strings using map
final_list = map(
    lambda s: f"{s[0]} - Average: {(s[1] + s[2]) / 2}", smart_students
)

print(list(final_list))