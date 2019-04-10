#!python

import string
import math
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

#so we're going to smush the digits and the ascii_lowercase together. This resultant long array will be accessible thru index and can be used to convert int -> string
all_digits = string.digits + string.ascii_lowercase

#enumerate: treat array like a DICT w/ (index of array, string) as the (key, value) pair.
#can't just scrap enumerate because it's not actually a dictionary
to_dict = {string: index for index, string in enumerate(all_digits)}

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base) #handle up to base36
    decoded = 0 #initialize. start w/ 0 here bc we're adding to it, no need to be empty

    for index, value in enumerate(reversed(digits)):
        decoded += (base**index) * to_dict[value]
    return decoded

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base) #handle up to base36
    assert number >= 0, 'number is negative: {}'.format(number) #handle unsigned numbers only for now
    encoded = '' #can't start w/ 0 bc this must be empty when we add to it
    big_power = math.floor(math.log(number, base))

    # -1, -1 BECAUSE:
    #the last -1 is the STEP (loop backwards in increments of 1). Default value: +1
    #the penultimate -1 is because range is not inclusive; without this -1, it starts at index 1, not 0.

    for i in range(big_power, -1, -1):
        if base**i <= number:
            quotient = number // (base**i)
            number -= quotient * (base**i)
            encoded += all_digits[quotient]
        else:
            encoded += '0'
    return encoded
            
    

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    return encode(decode(digits, base1), base2)

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()





# Code review 04.04.19


# def max_decode(digits, base): #Maximo's code review. Won't use. It's here for ref
#     #suggested:
#     #   - make 'alphabet' and 'digits' global-scope variables, as they'll likely be used by other fxns
#     #   - validate that the digit even exists in the base passed in
#     #       - ex. 'G' passed in with base 16 would return 16, not an error (as it should)
#     assert 2 <= base <= 36, 'base is out of range: {}'.format(base) #handle up to base36
#     alphabet = string.ascii_lowercase
#     digits = digits.lower() #make all lowercase for standardizing
#     exponent = len(digits) - 1 #don't surpass what you're counting! This is the maximum power to which the base is taken
#     num_result = 0 #instantiate

#     for digit in digits:
#         if digit.isnumeric(): #Alan's change
#         # if digit not in alphabet: #check if digit is not a letter
#             num_result += (base ** exponent) * int(digit) #'base**exponent' = 'pow(base, exponent)' in python
#             # exponent -= 1
#         elif digit in alphabet: #Alan's change
#         # else: #if you get a letter
#             hex_to_digit = ord(digit) - 87 #ORDinal: ascii char --> # that encodes it. The 87 is bc he lowercases all - if you don't lowercase it, you'll have a different number
#             digit = hex_to_digit
#             num_result += (base ** exponent) * int(digit)
#             # exponent -= 1
#         else:
#             raise ValueError('...')
#         exponent -= 1 #suggested change by classmate
#     return num_result
# 
# def sukhrob_decode(number, base):
#     dividend = number
#     divisor = base
#     quotient = 1
#     result = ''
#     while quotient != 0:
#         if dividend < divisor: #if dividend < divisor, no need to divide. so dividend = remaidner
#             remainder = dividend % divisor
#             quotient = 0
#         else:
#             remainder = dividend % divisor
#             dividend = (dividend - remainder) // divisor #updating the dividend until it's less than divisor
        
#         if remainder > 9:
#             #in ascii table, lowercase 'a' is at the number 97
#             #so adding 10 + 87 = 97 => 'a', 11 + 87 = 98 => 'b' and so on
#             remainder = chr(remainder + 87) #wow a magic number! Alan says set these equal to semantic variable names (ex. 'hex_letter_offset')

#         result += str(remainder)

#     return result[::-1] #flips the result at the end... because before return, result is in reverse order