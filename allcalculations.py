import math

# Function to perform calculations
def perform_calculations(numbers, operation):
    try:
        if operation == "sum":
            result = sum(numbers)
        elif operation == "subtract":
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
        elif operation == "multiply":
            result = 1
            for num in numbers:
                result *= num
        elif operation == "divide":
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    return "Error: Division by zero is not allowed."
                result /= num
        elif operation == "average":
            result = sum(numbers) / len(numbers)
        elif operation == "max":
            result = max(numbers)
        elif operation == "min":
            result = min(numbers)
        elif operation == "power":
            if len(numbers) != 2:
                return "Error: Power operation requires exactly two numbers."
            result = numbers[0] ** numbers[1]
        elif operation == "sqrt":
            if len(numbers) != 1:
                return "Error: Square root operation requires exactly one number."
            result = math.sqrt(numbers[0])
        elif operation == "modulus":
            if len(numbers) != 2:
                return "Error: Modulus operation requires exactly two numbers."
            result = numbers[0] % numbers[1]
        elif operation == "factorial":
            if len(numbers) != 1:
                return "Error: Factorial operation requires exactly one number."
            result = math.factorial(numbers[0])
        elif operation == "log":
            if len(numbers) != 1:
                return "Error: Logarithm operation requires exactly one number."
            result = math.log(numbers[0])
        else:
            return "Invalid operation. Please try again."
        return result
    except ValueError:
        return "Error: Invalid value provided."

# Main function to interact with the user
def main():
    print("Welcome to the Multi-Calculator!")
    try:
        # Prompt user for input
        numbers = list(map(float, input("Enter two or more numbers separated by spaces: ").split()))
        if len(numbers) == 0:
            print("You must enter at least two numbers.")
            return

        # List available operations
        print("\nAvailable operations:")
        print("1. sum - Add all numbers")
        print("2. subtract - Subtract all numbers from the first number")
        print("3. multiply - Multiply all numbers")
        print("4. divide - Divide the first number by subsequent numbers")
        print("5. average - Calculate the average of the numbers")
        print("6. max - Find the maximum number")
        print("7. min - Find the minimum number")
        print("8. power - Raise the first number to the power of the second")
        print("9. sqrt - Find the square root (only one number allowed)")
        print("10. modulus - Find the remainder of division (requires two numbers)")
        print("11. factorial - Calculate the factorial (only one number allowed)")
        print("12. log - Find the natural logarithm (only one number allowed)")

        # Choose operation
        operation = input("\nChoose an operation (e.g., sum, divide): ").strip().lower()

        # Perform calculation
        result = perform_calculations(numbers, operation)

        # Display result
        print(f"\nResult: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

# Execute the script
if __name__ == "__main__":
    main()
