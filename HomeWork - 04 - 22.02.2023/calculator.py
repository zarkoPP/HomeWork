# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

# Function to check if the user's choice of operation is valid
def is_valid_choice(choice):
    return choice in ["1", "2", "3", "4"]

# Function to check if the user's input is a valid number
def is_valid_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Function to format a floating point number with a specified number of decimal places
def format_float(num, num_decimals):
    return f"{num:.{num_decimals}f}"

# Main function that drives the calculator program
def calculator():
    while True:
        # Display the list of operations
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Get the user's choice of operation
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if the user wants to exit
        if choice == "5":
            break

        # Check if the user's choice of operation is valid
        if not is_valid_choice(choice):
            print("Error: Invalid input. Please enter a valid choice.")
            continue

        # Get the user's input for the numbers
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        # Check if the user's input is valid
        if not is_valid_number(num1) or not is_valid_number(num2):
            print("Error: Invalid input. Please enter a valid number.")
            continue

        # Convert the user's input to floating point numbers
        num1 = float(num1)
        num2 = float(num2)

        # Perform the operation based on the user's choice
        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)

            # Check if there was a division by zero error
            if isinstance(result, str):
                print(result)
                continue

        # Display the result to the user with different formatting options
        print(f"Result: {format_float(result, 1)}")
        print(f"Result: {format_float(result, 2)}")
        print(f"Result: {format_float(result, 3)}")
        print(f"Result: {format_float(result, 4)}")

# Call the calculator function to start the program
calculator()
