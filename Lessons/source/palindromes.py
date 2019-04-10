#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)

def is_palindrome_iterative(text):
    split_text = list(text)
    left = 0
    right = len(split_text)-1
    while left < right:
        if split_text[left] == split_text[right]:
            right -= 1
            left += 1
        else:
            return False
    else:
        return True

    # #lol no
    # split_text = list(text) #text -> array of characters
    # flipped_text = list(reversed(split_text))
    # if flipped_text == split_text:
    #     return True
    # else:
    #     return False

def is_palindrome_recursive(text, left=None, right=None):
    split_text = list(text)
    if left is None and right is None:
        left = 0
        right = len(split_text)-1
    elif left is None or right is None:
        raise AssertionError('Please specify either BOTH left and right params, or neither')
    if left < right:
        if split_text[left] == split_text[right]:
            return is_palindrome_recursive(text, left+1, right-1)
        else:
            return False
    else:
        return True

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            hooray = '🎉 BOOYAH 🎉' if is_pal else ''
            print('{}: {} {} a palindrome {}'.format(result, repr(arg), is_str, hooray))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()