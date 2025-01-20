import math
from typing import List, Union, Dict, Callable
from dataclasses import dataclass

@dataclass
class Operation:
    """Defines a calculator operation with its requirements and function."""
    func: Callable
    min_args: int
    max_args: int
    description: str

class Calculator:
    """Advanced calculator with multiple mathematical operations."""
    
    def __init__(self):
        """Initialize calculator with available operations."""
        self.operations: Dict[str, Operation] = {
            '1.sum': Operation(
                lambda nums: sum(nums),
                2, float('inf'), "Add all numbers"
            ),
            '2.subtract': Operation(
                lambda nums: nums[0] - sum(nums[1:]),
                2, float('inf'), "Subtract all numbers from the first number"
            ),
            '3.multiply': Operation(
                lambda nums: math.prod(nums),
                2, float('inf'), "Multiply all numbers"
            ),
            '4.divide': Operation(
                lambda nums: nums[0] / math.prod(nums[1:]) if not any(x == 0 for x in nums[1:]) 
                else "Error: Division by zero",
                2, float('inf'), "Divide first number by subsequent numbers"
            ),
            '5.average': Operation(
                lambda nums: sum(nums) / len(nums),
                1, float('inf'), "Calculate the average of numbers"
            ),
            '6.max': Operation(
                lambda nums: max(nums),
                1, float('inf'), "Find the maximum number"
            ),
            '7.min': Operation(
                lambda nums: min(nums),
                1, float('inf'), "Find the minimum number"
            ),
            '8.power': Operation(
                lambda nums: nums[0] ** nums[1],
                2, 2, "Raise first number to power of second"
            ),
            '9.sqrt': Operation(
                lambda nums: math.sqrt(nums[0]) if nums[0] >= 0 
                else "Error: Cannot calculate square root of negative number",
                1, 1, "Calculate square root of number"
            ),
            '10.modulus': Operation(
                lambda nums: nums[0] % nums[1] if nums[1] != 0 
                else "Error: Modulus by zero",
                2, 2, "Find remainder of division"
            ),
            '11.factorial': Operation(
                lambda nums: math.factorial(int(nums[0])) if nums[0] >= 0 and nums[0].is_integer()
                else "Error: Factorial requires non-negative integer",
                1, 1, "Calculate factorial of number"
            ),
            '12.log': Operation(
                lambda nums: math.log(nums[0]) if nums[0] > 0 
                else "Error: Logarithm requires positive number",
                1, 1, "Calculate natural logarithm"
            )
        }

    def validate_input(self, numbers: List[float], operation: str) -> Union[str, None]:
        """Validate input numbers and operation."""
        if operation not in self.operations:
            return "Error: Invalid operation"
        
        op = self.operations[operation]
        if len(numbers) < op.min_args:
            return f"Error: {operation} requires at least {op.min_args} number(s)"
        if len(numbers) > op.max_args:
            return f"Error: {operation} accepts maximum {op.max_args} number(s)"
        
        return None

    def calculate(self, numbers: List[float], operation: str) -> Union[float, str]:
        """Perform calculation based on operation."""
        validation_error = self.validate_input(numbers, operation)
        if validation_error:
            return validation_error

        try:
            return self.operations[operation].func(numbers)
        except Exception as e:
            return f"Error: {str(e)}"

    def get_operations_menu(self) -> str:
        """Generate menu of available operations."""
        menu = "\nAvailable operations:"
        for op, details in self.operations.items():
            menu += f"\n{op} - {details.description}"
        return menu

def get_numbers() -> Union[List[float], str]:
    """Get and validate number input from user."""
    try:
        numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
        if not numbers:
            return "Error: No numbers entered"
        return numbers
    except ValueError:
        return "Error: Invalid number format"

def main():
    """Main program loop."""
    calculator = Calculator()
    empty_input_count = 0
    
    print("Welcome to the Advanced Calculator!")
    
    while True:
        print("\n" + "="*50)
        numbers = get_numbers()
        if isinstance(numbers, str):
            if numbers == "Error: No numbers entered":
                empty_input_count += 1
                if empty_input_count == 3:
                    choice = input("You have pressed Enter without input 3 times. Do you want to quit? (yes/no): ").strip().lower()
                    if choice == "yes":
                        print("\nThank you for using the Advanced Calculator!")
                        break
                    else:
                        empty_input_count = 0
                        continue
            else:
                print(numbers)
                continue
        else:
            empty_input_count = 0

        print(calculator.get_operations_menu())
        operation = input("\nChoose an operation (or 'quit' to exit): ").strip().lower()
        
        if operation == 'quit':
            print("\nThank you for using the Advanced Calculator!")
            break

        # Allow user to input the operation number or name
        operation_key = next((key for key in calculator.operations if operation in key), None)
        if not operation_key:
            print("Error: Invalid operation")
            continue

        result = calculator.calculate(numbers, operation_key)
        print(f"\nResult: {result}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCalculator terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
