# test_exception_handling.py

import slash
from slash.exception_handling import handling_exceptions

def critical_operation(number, divisor):
    if divisor == 0:
        slash.add_error("Cannot divide by zero")
    else:
        pass

def perform_critical_operation_safely():
    with handling_exceptions():
        critical_operation(10, 0)

# Test the database operation
def test_database_operation():
    perform_critical_operation_safely()
