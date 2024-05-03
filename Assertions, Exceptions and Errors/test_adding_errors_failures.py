# test_adding_errors_failures.py

import slash

def check_divisibility(number, divisor):
    if divisor == 0:
        slash.add_error("Cannot divide by zero")
    elif number % divisor != 0:
        slash.add_failure(f"{number} is not divisible by {divisor}")

class MyTest(slash.Test):
    def test_divisibility(self):
        numbers = [10, 20, 30]
        divisors = [2, 3, 0, 5]  # Intentionally include a divisor of 0 for testing error reporting
        
        for number in numbers:
            for divisor in divisors:
                check_divisibility(number, divisor)

        # Other assertions or code can continue here...
