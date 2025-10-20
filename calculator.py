"""
Simple Calculator Module
Provides basic arithmetic operations: addition, subtraction, multiplication, and division.
"""


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """
    Divide a by b and return the result.
    
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b and return the result."""
    return a ** b


def main():
    """Main function to run the calculator in interactive mode."""
    print("Welcome to the Simple Calculator!")
    print("Available operations: add, subtract, multiply, divide, power, quit")
    
    while True:
        operation = input("\nEnter operation: ").strip().lower()
        
        if operation == "quit":
            print("Thank you for using the calculator!")
            break
        
        if operation not in ["add", "subtract", "multiply", "divide", "power"]:
            print("Invalid operation. Please try again.")
            continue
        
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if operation == "add":
                result = add(a, b)
            elif operation == "subtract":
                result = subtract(a, b)
            elif operation == "multiply":
                result = multiply(a, b)
            elif operation == "divide":
                result = divide(a, b)
            elif operation == "power":
                result = power(a, b)
            
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
