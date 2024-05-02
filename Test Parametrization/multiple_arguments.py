# multiple_arguments.py

import slash

@slash.parametrize(('fruit', 'color'), [('apple', 'red'), ('apple', 'green'), ('banana', 'yellow')])
def test_fruits(fruit, color):
    print(fruit + ' has color: ' + color)
    pass # <-- this never gets a yellow apple
