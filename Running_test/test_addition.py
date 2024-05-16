# test_addition.py

def test_safe_addition():
    assert 2 + 2 == 4

def test_dangerous_addition():
    assert 3 + 3 == 6


# slash run test_addition.py
# slash run -v test_addition.py
# slash run -q test_addition.py
# slash run -tb=2 test_addition.py (-tp can be 0~5)
