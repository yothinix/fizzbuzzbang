from fizzbuzz import fizzbuzz


def test_input_3_should_return_fizz():
    number = 3
    expected = 'fizz'

    actual = fizzbuzz(number)

    assert actual == expected


def test_input_5_should_return_buzz():
    number = 5
    expected = 'buzz'

    actual = fizzbuzz(number)

    assert actual == expected


def test_input_6_should_return_fizz():
    number = 6
    expected = 'fizz'

    actual = fizzbuzz(number)

    assert actual == expected


def test_input_10_should_return_buzz():
    number = 10
    expected = 'buzz'

    actual = fizzbuzz(number)

    assert actual == expected


def test_input_15_should_return_fizzbuzz():
    number = 15
    expected = 'fizzbuzz'

    actual = fizzbuzz(number)

    assert actual == expected


def test_input_1_should_return_1():
    number = 1
    expected = '1'

    actual = fizzbuzz(number)

    assert actual == expected


def test_input_4_should_return_list_of_result():
    number = 4
    expected = ['1', '2', 'fizz', '4']

    actual = fizzbuzz(number)

    assert actual == expected


def test_input_7_should_return_bang():
    number = 7
    expected = 'bang'

    actual = fizzbuzz(number)

    assert actual == expected


def test_input_8_should_return_list_reverse():
    number = 8
    expected = ['8', 'bang', 'fizz', 'buzz', '4', 'fizz', '2', '1']

    actual = fizzbuzz(number)

    assert actual == expected
