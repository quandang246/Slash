# test_example.py

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 3 - 1 == 2

def test_multiplication():
    assert 2 * 2 == 4

def test_division():
    assert 4 / 2 == 2

def test_exponential():
    assert 2 ** 3 == 8

def test_failing_operation():
    assert 2 * 3 == 5  # Intentional failure

def test_component_one():
    assert True

def test_component_two():
    assert True


# slash run -v -k division test_including_excluding.py
# slash run -v -k "not failing_" test_including_excluding.py 
