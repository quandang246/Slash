# sum_even.py

import slash

def test_sum_even_numbers():
    input_num = int(input("Enter positive integer:"))

    even_sum = sum(x for x in range(2, input_num + 1, 2))
    print(f"The sum of even numbers from 1 to {input_num} is: {even_sum}")

    pass
