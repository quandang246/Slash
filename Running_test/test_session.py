# test_session.py

from slash import session

print("The current session id is", session.id)

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

def test_failing_addition():
    assert 2 + 3 == 10  # Intentional failure


def test_failing_subtraction():
    assert 2 - 3 == 5  # Intentional failure

def test_component_one():
    assert True

def test_component_two():
    assert True


# slash run -v test_session.py
# slash resume -vv 7cab1801-085a-11ef-b8d0-dc41a9d9f679_
# slash resume -vv --failed-first 7cab1801-085a-11ef-b8d0-dc41a9d9f679_
# slash resume -vv --unstarted-first 7cab1801-085a-11ef-b8d0-dc41a9d9f679_

