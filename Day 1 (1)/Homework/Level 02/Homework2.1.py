# 1) ფუნქცია input() ყოველთვის აბრუნებს ტექსტს (string). 
# როდესაც ვწერთ input() - 0, ეს გამოიწვევს შეცდომას (Error), 
# რადგან ტექსტს ვერ გამოვაკლებთ რიცხვს. 
# თუ გვინდა მათემატიკური მოქმედება, ტექსტი უნდა ვაქციოთ რიცხვად int() ფუნქციით.

# 2) მათემატიკური ოპერაციები:
# +  დამატება (მიმატება)
# -  გამოკლება
# * გამრავლება
# /  გაყოფა (აბრუნებს ათწილადს)
# // მთელი რიცხვის მიღება გაყოფისას (ჭრის ნაშთს)
# %  ნაშთიანი გაყოფა (აბრუნებს მხოლოდ ნაშთს)
# ** ხარისხში აყვანა

# 3) მომხმარებლის მონაცემების შეყვანა
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
fav_number = input("Enter your favorite number: ")

print("name:", first_name)
print("last name:", last_name)
print("age:", age)
print("favorite number:", fav_number)

print("---") # ვიზუალური დაყოფისთვის

# 4) მათემატიკური ოპერაციები 3 რიცხვზე
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("Sum:", num1 + num2 + num3)
print("Difference:", num1 - num2 - num3)
print("Product:", num1 * num2 * num3)
print("Division:", num1 / num2 / num3)

# 5) განსხვავება Frontend-სა და Backend-ს შორის:
# Frontend (ფრონტენდი) არის ის, რასაც მომხმარებელი ხედავს და რასთანაც ინტერაქციაში შედის (ღილაკები, დიზაინი).
# Backend (ბექენდი) არის "კულისებს მიღმა" მომუშავე ნაწილი - მონაცემთა ბაზები, სერვერები და ლოგიკა.