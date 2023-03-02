
def number_to_numeral(number):
    # def is defining a function called number_to_numeral
    # number is the vaule
    """
    >>> number_to_numeral(1)
    'I'
    >>> number_to_numeral(2)
    'II'
    >>> number_to_numeral(12)
    'XII'
    >>> number_to_numeral(10)
    'X'
    >>> number_to_numeral(20)
    'XX'
    >>> number_to_numeral(99)
    'XCIX'
    >>> number_to_numeral(100)
    'C'
    >>> number_to_numeral(199)
    'CXCIX'
    >>> number_to_numeral(2399)
    'MMCCCXCIX'
    >>> number_to_numeral(4000)
    Traceback (most recent call last):
    ...
    IndexError: list index out of range

    """
# lines 4 to 28 is the function being defined
# when the vaule is a number then it show what is in ""

    numerals_dict = {
        'ones':     ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        'tens':     ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        'hundreds': ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        'thousands': ['', 'M', 'MM', 'MMM'],
    }
# lines 33 to 38 are a dictionary
# one is the key, and within the [] are the vaules
# when 1 is entered it should change to I

    s = []
# this is a list called s
    for index in ['ones', 'tens', 'hundreds', 'thousands']:
        # index is a variable, so we are saying for index in one of the key vaules do this
        number, remainder = divmod(number, 10)
# when the vaule number is give & its remainders divide by 10
        s.insert(0, numerals_dict[index][remainder])
# s is the varible, insert is the action
# within the parathesis it's telling python to use numberals_dict then divide with inden then define the remainder
    return ''.join(s)
# return takes the vaule inside the function and sends it back to the line
# .join is taking 's' together into one string
