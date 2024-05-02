# labeling_parameters.py

import slash

# default 
@slash.parametrize('param', [1, 2])
def test_number(param):
    pass

@slash.parametrize('param', [
  slash.param('first', 1),
  slash.param('second', 2),
])
def test_something(param):
    pass

"""
The two forms are functionally equivalent:

@slash.parametrize('param', [
  1 // slash.param('first'),
  2 // slash.param('second'),
])
def test_something(param):
    pass
"""
