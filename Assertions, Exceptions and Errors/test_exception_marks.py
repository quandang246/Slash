# test_exception_marks.py

import slash
import slash.exception_handling
from slash.exception_handling import (
    noswallow,
    disable_exception_swallowing,
    )
from slash.exception_handling import inhibit_unhandled_exception_traceback

# Fatal Exceptions
def divide (num1, num2):
    if num2 == 0:
        # raise slash.exception_handling.mark_exception_fatal(Exception('Dividing zero!'))
        # slash.add_error("Dividing zero!").mark_fatal()      
        return 0
    else:
        return num1/num2
    
def test_divide():  # will terminate right after fatal exception
    divide(5,0)


# Exception Swallowing 
# Usage
def attempt_to_upload_logs():
    with slash.get_exception_swallowing_context():
        # Actual operations here
        pass

# Force certain exceptions through by using the noswallow() or disable_excception_swallowing
def func1():
   raise noswallow(Exception("CRITICAL!"))

def func2():
   e = Exception("CRITICAL!")
   disable_exception_swallowing(e)
   raise e

@disable_exception_swallowing
def func3():
   raise Exception("CRITICAL!")
"""
def test_func():
    func1()
    func2()
    func3()
"""

# Console Traceback of Unhandled Exceptions
def func4():
    try:
        raise Exception("A!")
        # raise inhibit_unhandled_exception_traceback(Exception('Critical!'))
    except Exception as e:
        print ("An error occurred:", e)

def test_func4():
    func4()
