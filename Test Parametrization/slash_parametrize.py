# test.py

import slash

# basic usage - 1 test
@slash.parametrize('x', [1, 2, 3])
def test_something(x):
    pass

# Parametrizing Before, Test, and After methods - 3x3x3 = 27 tests 
class SomeTest(slash.Test):
    @slash.parametrize('x', [1, 2, 3])
    def before(self, x):
        pass

    @slash.parametrize('y', [4, 5, 6])
    def test(self, y):
        pass

    @slash.parametrize('z', [7, 8, 9])
    def after(self, z):
        pass


# Inheritance
class BaseTest(slash.Test):

    @slash.parametrize('base_parameter', [1, 2, 3])
    def before(self, base_parameter):
        pass

class DerivedTest(BaseTest):

    @slash.parametrize('derived_parameter', [4, 5, 6])
    def before(self, derived_parameter):
        super(DerivedTest, self).before(derived_parameter)  # Pass the parameter here
        pass
