# excluding_parameters.py

import slash

SUPPORTED_SIZES = [10, 15, 20, 25]

@slash.parametrize('size', SUPPORTED_SIZES)
@slash.exclude('size', [10, 20])
def test_size (size):   # <-- will be skipped for sizes 10 and 20
    pass

@slash.parametrize('size', SUPPORTED_SIZES)
@slash.fixture
def car(size): # <-- will be skipped for sizes 10 and 20
    pass

SUPPORTED_SIZES = [10, 15, 20, 25]
@slash.exclude(('car.size', 'car.color'), [(10, 'red'), (20, 'blue')])
def test_car(car):
    pass
@slash.parametrize('size', SUPPORTED_SIZES)
@slash.parametrize('color', ['red', 'green', 'blue'])
@slash.fixture
def car(size, color): # <-- red cars of size 10 and blue cars of size 20 will be skipped
    pass
