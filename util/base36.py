# following code is taken from:
# https://stackoverflow.com/questions/1181919/python-base-36-encoding


def base36encode(number):
    # changed this as was throwing error when no number to convert
    if not isinstance(number, (int)):
        return "  "
    if number < 0:
        raise ValueError('number must be positive')

    alphabet, base36 = ['0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', '']

    while number:
        number, i = divmod(number, 36)
        base36 = alphabet[i] + base36

    return base36 or alphabet[0]


def base36decode(number):
    return int(number, 36)

