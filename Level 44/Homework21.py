#4)
def calculate_discount():
    try:
        price = float(input("Enter price here: "))
        discount = float(input("Enter discount by percents (%): "))
        discount_amount = price * (discount / 100)
    except ValueError:
        print("Ahp- Enter numbers only!")
    else:
        print(f"Discounted amount: {discount_amount}")

#5)
def square_elements(lst):
    try:
        new_list = []
        for x in lst:
            new_list.append(x ** 2)
    except TypeError:
        print("Sorry, but the list must contain only numbers!")

#6)
def get_average(numbers, index):
    try:
        val = numbers[index]
        res = 100 / val
    except IndexError:
        print("Naiy, invalid index!")
    except ZeroDivisionError:
        print("Naiy, I don't have a right to divide it by zero!")
    finally:
        print("Calculation complete! Well done.")