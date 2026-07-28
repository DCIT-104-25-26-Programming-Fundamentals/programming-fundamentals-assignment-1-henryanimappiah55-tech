# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def show_menu():
    """Display the menu options."""
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Return a / b, or None if b is zero."""
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Return a % b, or None if b is zero."""
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    return a ** b


def get_two_numbers():
    """Prompt for and return two numbers as floats."""
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    return a, b


def main():
    symbols = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
        "5": "%",
        "6": "**"
    }

    while True:
        show_menu()
        choice = input("Select an operation (1-7): ")
        print()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in symbols:
            print("Error: Invalid choice. Please enter a number from 1 to 7.")
            print()
            continue

        a, b = get_two_numbers()
        symbol = symbols[choice]

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
            if result is None:
                print("Error: Cannot divide by zero.")
                print()
                continue
        elif choice == "5":
            result = modulus(a, b)
            if result is None:
                print("Error: Cannot divide by zero.")
                print()
                continue
        elif choice == "6":
            result = exponentiate(a, b)

        # Clean up whole-number floats (e.g. 13.0 -> 13) for nicer display
        if result == int(result):
            result = int(result)

        print(f"Result: {a:g} {symbol} {b:g} = {result}")
        print()



main()