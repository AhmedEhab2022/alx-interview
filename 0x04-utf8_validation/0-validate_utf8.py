#!/usr/bin/python3
"""UTF-8 Validation problem
"""


def validUTF8(data):
    """Method that determines if a given data set represents a valid
    UTF-8 encoding.
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to
    handle the 8 least significant bits of each integer
    """
    count = 0
    for num in data:
        binaryStr = f'{num:08b}'
        if count > 0:
            if binaryStr[:2] != '10':
                return False
            count -= 1
        else:
            if binaryStr[0] == '0':
                continue
            elif binaryStr[:3] == '110':
                count = 1
            elif binaryStr[:4] == '1110':
                count = 2
            elif binaryStr[:5] == '11110':
                count = 3
            else:
                return False

    return count == 0
