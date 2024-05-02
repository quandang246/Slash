# toggle_iterate.py

import slash

@slash.parameters.toggle('with_safety_switch')
def test_operation(with_safety_switch):
    if with_safety_switch:
        assert 1 + 1 == 2
        pass
    else:
        assert 2 + 2 == 4
        pass

@slash.parameters.iterate(x=[1, 2, 3], y=[4, 5, 6])
def test_something(x, y):
    # Test logic using x and y
    pass
