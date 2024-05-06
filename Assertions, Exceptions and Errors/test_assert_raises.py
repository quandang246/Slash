import slash

def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return numerator / denominator

with slash.assert_raises(ZeroDivisionError) as caught:          # slash.assert_raises()
    divide(5, 0)
    # divide(5,1) will raise <Error: slash.exceptions.ExpectedExceptionNotCaught: ZeroDivisionError not raised>

assert str(caught.exception) == "Cannot divide by zero"         

"""
with slash.allowing_exceptions(ZeroDivisionError) as caught:    # slash.assert_raises()
    pass

slash.assert_almost_equal(1.001, 1, delta=0.1)                  # slash.allowing_exceptions()
"""
def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return numerator / denominator

import slash

with slash.assert_raises(ZeroDivisionError) as caught:          # slash.assert_raises()
    divide(5, 0)

assert str(caught.exception) == "Cannot divide by zero"         


with slash.allowing_exceptions(ZeroDivisionError) as caught:    # slash.assert_raises()
    pass

slash.assert_almost_equal(1.001, 1, delta=0.1)                  # slash.allowing_exceptions()
