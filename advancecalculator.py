import math
from typing import List, Union, Dict, Callable
from enum import Enum

class Operation(Enum):
    SUM = ('1', 'sum', 'add')
    SUBTRACT = ('2', 'subtract', 'sub')
    MULTIPLY = ('3', 'multiply', 'mul')
    DIVIDE = ('4', 'divide', 'div')
    AVERAGE = ('5', 'average', 'avg')
    MAX = ('6', 'max', 'maximum')
    MIN = ('7', 'min', 'minimum')
    POWER = ('8', 'power', 'pow')
    SQRT = ('9', 'sqrt', 'square root')
    MODULUS = ('10', 'modulus', 'mod')
    FACTORIAL = ('11', 'factorial', 'fact')
    LOG = ('12', 'log', 'logarithm')

class Calculator:
    def __init__(self):
        self.operations: Dict[Operation, Callable] = {
            Operation.SUM: self.sum_numbers,
            Operation.SUBTRACT: self.subtract_numbers,
            Operation.MULTIPLY: self.multiply_numbers,
            Operation.DIVIDE: self.divide_numbers,
            Operation.AVERAGE: self.average_numbers,
            Operation.MAX: self.max_number,
            Operation.MIN: self.min_number,
            Operation.POWER: self.power_numbers,
            Operation.SQRT: self.sqrt_number,
            Operation.MODULUS: self.modulus_numbers,
            Operation.FACTORIAL: self.factorial_number,
            Operation.LOG: self.log_number
        }
        
        self.operation_requirements = {
            Operation.POWER: 2,
            Operation.SQRT: 1,
            Operation.MODULUS: 2,
            Operation.FACTORIAL: 1,
            Operation.LOG: 1
        }

    def validate_numbers(self, numbers: List[float], operation: Operation) -> str:
        """Validate the input numbers for the given operation."""
        if not numbers:
            return "Error: No numbers provided."
            
        required_count = self.operation_requirements.get(operation)
        if required_count and len(numbers) != required_count:
            return f"Error: {operation.name.lower()} operation requires exactly {required_count} number(s)."
            
        return ""

    def sum_numbers(self, numbers: List[float]) -> float:
        return sum(numbers)

    def subtract_numbers(self, numbers: List[float]) -> float:
        return numbers[0] - sum(numbers[1:])

    def multiply_numbers(self, numbers: List[float]) -> float:
        result = 1
        for num in numbers:
            result *= num
        return result

    def divide_numbers(self, numbers: List[float]) -> Union[float, str]:
        if any(num == 0 for num in numbers[1:]):
            return "Error: Division by zero is not allowed."
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
        return result

    def average_numbers(self, numbers: List[float]) -> float:
        return sum(numbers) / len(numbers)

    def max_number(self, numbers: List[float]) -> float:
        return max(numbers)

    def min_number(self, numbers: List[float]) -> float:
        return min(numbers)

    def power_numbers(self, numbers: List[float]) -> float:
        return numbers[0] ** numbers[1]

    def sqrt_number(self, numbers: List[float]) -> Union[float, str]:
        if numbers[0] < 0:
            return "Error: Cannot calculate square root of negative number."
        return math.sqrt(numbers[0])

    def modulus_numbers(self, numbers: List[float]) -> Union[float, str]:
        if numbers[1] == 0:
            return "Error: Cannot calculate modulus with zero."
        return numbers[0] % numbers[1]

    def factorial_number(self, numbers: List[float]) -> Union[int, str]:
        if numbers[0] < 0 or not numbers[0].is_integer():
            return "Error: Factorial requires a non-negative integer."
        return math.factorial(int(numbers[0]))

    def log_number(self, numbers: List[float]) -> Union[float, str]:
        if numbers[0] <= 0:
            return "Error: Cannot calculate logarithm of non-positive number."
        return math.log(numbers[0])

    def get_operation(self, user_input: str) -> Union[Operation, None]:
        """Match user input to an operation."""
        user_input = user_input.lower().strip()
        for operation in Operation:
            if user_input in operation.value:
                return operation
        return None

def main():
    calculator = Calculator()
    
    print("Welcome to the Multi-Calculator!")
    print("\nAvailable operations:")
    for operation in Operation:
        print(f"{operation.value[0]}. {operation.value[1]} - {operation.value[2]}")

    try:
        # Get numbers from user
        numbers_input = input("\nEnter numbers separated by spaces: ")
        numbers = [float(x) for x in numbers_input.split()]

        # Get operation from user
        operation_input = input("Choose an operation (number or name): ").strip()
        operation = calculator.get_operation(operation_input)

        if not operation:
            print("Error: Invalid operation selected.")
            return

        # Validate numbers for the operation
        validation_error = calculator.validate_numbers(numbers, operation)
        if validation_error:
            print(validation_error)
            return

        # Perform calculation
        result = calculator.operations[operation](numbers)
        print(f"\nResult: {result}")

    except ValueError as e:
        print(f"Error: Invalid input. Please enter valid numbers. ({str(e)})")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()