def add(num1, num2):
    """
    Function to add two numbers
    """
    return num1 + num2


def subtract(num1, num2):
    """
    Function to subtract two numbers
    """
    return num1 - num2


def multiply(num1, num2):
    """
    Function to multiply two numbers
    """
    return num1 * num2


def divide(num1, num2):
    """
    Function to divide two numbers
    """
    if num2 == 0:
        # Division by zero error handling
        return "Error: Division by zero"
    return num1 / num2


def get_valid_number(prompt):
    """
    Function to get a valid number input from the user
    """
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            # Check for valid inputs - only numbers allowed
            print("Error: Invalid input. Please enter a valid number.")


def calculator():
    """
    Function to present a simple calculator interface to the user
    """
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")
        if choice == "5":
            # Exit the program if user chooses 5
            break

        # Check whether the choice is valid
        if choice not in ["1", "2", "3", "4"]:
            print("Error: Invalid input. Please enter a valid choice.")
            continue

        num1 = get_valid_number("Enter first number: ")
        num2 = get_valid_number("Enter second number: ")

        # Call the appropriate function based on the user's choice
        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)

            # Print an error message if division by zero occurs
            if isinstance(result, str):
                print(result)
                continue

        # Try different formatting for the floating point numbers
        print(f"Result: {result:.2f}") # 2 numbers after the decimal

        # Ask the user if they want to continue or exit the program
        choice = input("Do you want to perform another calculation? (y/n): ")
        if choice.lower() not in ["y", "yes"]:
            break


# Main program
calculator()
