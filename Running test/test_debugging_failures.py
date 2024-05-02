# test_debugging_failures.py

def test_passing_case():
    assert 1 + 1 == 2

def test_failing_case():
    assert 2 * 3 == 5  # Intentional failure


# slash run --pdb test_debugging_failures.py
