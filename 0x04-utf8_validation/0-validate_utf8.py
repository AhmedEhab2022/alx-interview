#!/usr/bin/python3
"""UTF-8 Validation problem
"""


def validUTF8(data):
    """method that determines if a given data set represents a valid
    UTF-8 encoding.
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data
    """
    count = 0
    for num in data:
        binaryStr = f'{num:08b}'
        if count > 0 and binaryStr[:2] != '10':
            return False
        elif count > 0 and binaryStr[:2] == '10':
            count -= 1
        elif count == 0 and binaryStr[:2] == '10':
            return False
        elif count == 0:
            for binaryChar in binaryStr:
                if binaryChar == '0':
                    break
                else:
                    count += 1
            count -= 1
    if count > 0:
        return False
    return True
