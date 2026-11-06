#16)
books = [
    {"title": "Python Basics", "pages": 120, "available": True},
    {"title": "JavaScript", "pages": 350, "available": False},
    {"title": "HTML Guide", "pages": 80, "available": True},
    {"title": "Advanced Python", "pages": 500, "available": True}
]

result = list(filter(lambda b: b["available"] and b["pages"] > 100, books))
print(result)

#17)
employees = ["Leo_Kvachadze", "Levan_Rcheulishvili", "Elguja_Amashukeli", "Mukhran_Machavariani"]
salaries = [1500, 2000, 1800, 2500]
bonuses = [200, 300, 150, 500]

for name, salary, bonus in zip(employees, salaries, bonuses):
    final_salary = salary + bonus
    print(f"{name}: {final_salary}")

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