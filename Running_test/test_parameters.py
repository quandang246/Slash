import slash

@slash.parameters.toggle('with_power_operator')
def test_power_of_two(with_power_operator):
    num = 2
    if with_power_operator:
        result = num ** 2
    else:
        result = num * num
    assert result == 4
