
"""Simple interactive Python script."""

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    name = input("What's your name? ").strip() or "there"
    print(f"Hello, {name}!")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print(f"{a} + {b} = {a + b}")

if __name__ == "__main__":
    main()

"""Simple interactive Python script."""

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    name = input("What's your name? ").strip() or "there"
    print(f"Hello, {name}!")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print(f"{a} + {b} = {a + b}")

if __name__ == "__main__":
    main()