#6)
def check_numbers(*args):
    print("Even numbers:")
    for num in args:
        if num % 2 == 0:
            print(num)

    print("Odd numbers:")
    for num in args:
        if num % 2 != 0:
            print(num)


check_numbers(1, 2, 3, 4, 5, 6, 7, 8)

#7)
def check_grade():
    score = int(input("Enter a score between 0 and 100: "))

    match score:
        case s if 90 <= s <= 100:
            print("Excellent")
        case s if 70 <= s <= 89:
            print("Good")
        case s if 50 <= s <= 69:
            print("Average")
        case s if 0 <= s <= 49:
            print("Failed")
        case _:
            print("Invalid grade")

check_grade()

#8)
def manage_names(*args):
    action = input("Enter an action (show, count, first, last): ")

    match action:
        case "show":
            print(args)
        case "count":
            print("Number of names:", len(args))
        case "first":
            if args:
                print("First name:", args[0])
            else:
                print("No names provided")
        case "last":
            if args:
                print("Last name:", args[-1])
            else:
                print("No names provided")
        case _:
            print("Invalid choice")


manage_names("Leo and Nodar Gabunias", "Varlam Topuria", "Ermile Bedia", "Mikheil Ipolitov-Ivanovi")

#9)
def calculate_prices(*args):
    if not args:
        print("No prices provided.")
        return

    total = sum(args)
    most_expensive = max(args)
    cheapest = min(args)
    average = total / len(args)

    print("Total price:", total)
    print("Most expensive:", most_expensive)
    print("Cheapest:", cheapest)
    print("Average price:", average)

calculate_prices(19.99, 5.50, 45.00, 12.75)

#10)
def manage_numbers(*args):
    if not args:
        print("No numbers provided.")
        return

    action = input("Enter an action (sum, max, min, even, odd, average, reverse): ")

    match action:
        case "sum":
            print("Sum:", sum(args))
        case "max":
            print("Max:", max(args))
        case "min":
            print("Min:", min(args))
        case "even":
            evens = [n for n in args if n % 2 == 0]
            print("Even numbers:", evens)
        case "odd":
            odds = [n for n in args if n % 2 != 0]
            print("Odd numbers:", odds)
        case "average":
            print("Average:", sum(args) / len(args))
        case "reverse":
            print("Reversed order:", args[::-1])
        case _:
            print("Invalid command")

manage_numbers(10, 15, 20, 25, 30)