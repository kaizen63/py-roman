
import sys
import collections


def int_to_roman(n: int):
    """Convert an Integer to a Roman Number
    """
    if n < 1:
        raise ValueError('Not a valid number: ' + str(n))
    
    # +------+-----+-----+-----+-----+-----+-----+-----+-----+------+
    # | Char |  I  |  V  |  X  |  L  |  C  |  D  |  M  |  ↁ  |  ↂ  |
    # | Value|  1  |  5  | 10  | 50  | 100 | 500 | 1000| 5000| 10000|
    # +------+-----+-----+-----+-----+-----+-----+-----+-----+------+
    romans_map = collections.OrderedDict(
        IIIII= 'V',
        IIII=  'IV', # subtraction rule
        VV=    'X',
        VIV=   'IX',
        XXXXX= 'L',
        XXXX=  'XL',
        LL=    'C',
        LXL=   'XC',
        CCCCC= 'D',
        CCCC=  'CD',
        DD=    'M',
        DCD=   'CM',
        MMMMM= 'ↁ',
        MMMM=  'Mↁ',
        ↁↁ=   'ↂ',
    )
    
    roman_str = 'I' * n
    for roman in romans_map.keys():
        roman_str = roman_str.replace(roman, romans_map[roman])
    return roman_str


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        print(f'{arg} converted to roman = {int_to_roman(int(arg))}')
