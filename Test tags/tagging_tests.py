# tagging_tests.py

import slash

failing = slash.tag('failing')

@slash.tag('dangerous')
def test_something():
    pass

@failing
def test_failing_something():
    assert 1+1 == 3

@slash.tag('covers', 'requirement_1294')   # covers will have value requirement_1294
def test_req_something():
    pass

# slash run -v tagging_tests.py
# slash run -v -k dangerous tagging_tests.py
# slash run -v -k tag:dangerous tagging_tests.py
# slash run -v -k "something and not tag:failing" tagging_tests.py
# slash run -v -k tag:covers=requirement_1294 tagging_tests.py



