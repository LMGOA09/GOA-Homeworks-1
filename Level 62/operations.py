def divide(a, b):
    if b == 0:
        return "Error: Division by zero is strictly prohibited!"
    return a / b

def power(a, b):
    return a**b

if __name__ == "__main__":
    print("Testing operations module directly:")
    print("10 / 2=", divide(10, 2))
    print("2 ^ 3 =", power(2, 3))