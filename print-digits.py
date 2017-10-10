"""Given int, print each digit in reverse order, starting with the ones place.

For example::

    >>> print_digits(1)
    1

    >>> print_digits(413)
    3
    1
    4

    >>> print_digits(7331)
    1
    3
    3
    7

"""


def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""

    # CAN'T USE STRING MANIPULATION; USE MATH
    # need to figure out how to strip 413 to its ones place and print that
    # modulo involved? dividing by 1/10/100 will give remainder of ones place
    # loop through num, stripping 413 --> 41 --> 4

    while num:
        next_digit = num % 10
        print next_digit
        num = (num - next_digit) / 10


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WOWZA!\n"
