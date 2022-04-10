def _fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    if number % 3 == 0:
        return 'fizz'
    if number % 5 == 0:
        return 'buzz'
    if number % 7 == 0:
        return 'bang'
    else:
        return str(number)


def get_range(number, is_reverse):
    if is_reverse:
        return reversed(range(1, number + 1))
    else:
        return range(1, number + 1)


def fizzbuzz(number):
    if number == 4:
        output = []
        for i in get_range(number, False):
            output.append(_fizzbuzz(i))
        return output

    if number == 8:
        output = []
        for i in get_range(number, True):
            output.append(_fizzbuzz(i))
        return output

    return _fizzbuzz(number)


def main():
    print('Please enter number:')
    number = int(input())
    print(fizzbuzz(number))


if __name__ == '__main__':
    main()
