# prime_check.py

import slash

def prime_number(input_num: int):
    if input_num > 1:
        for i in range(2, (input_num//2)+1):
            if (input_num % i) == 0:
                return False
                break
        return True
    else:
        return False

def test_prime():
    input_num = int(input("Enter number: "))

    assert prime_number(input_num) == True
