#!python
import collections
from collections import deque

#i did refactor this - credit to Ryan Nguyen for helping me understand I overcomplicating everything conceptually. So I was able to DRY the originally very wet code (get it? get it? ha ha ha)
#text=haystack, pattern=needle
def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    #funny storytime! initially did not pass because I falsely remembered a lack of explicitly written "else" statement resulting in a default return of "False". In truth, it defaults to "None"
    #Runtime: O(n) because it must go through text to find the pattern. Best case would be O(1), like if the pattern/needle was at the very front of the text/haystack.
    #Space: O(1) because it will always be simply true or false. Boolean, boom!
    if pattern in text:
        return True
    else:
        return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    #Runtime: O(n) because it must duplicated the array AND go through the-now quasi-dictionarified text. Each of these is O(n), adding to O(2n), but because runtime is about estimations and not exact figures, it's ultimately just O(n).
    #Space: O(1). Either 'None' or 'index' is returned, and no matter what the parameters, the size of output will remain the same

    for index, _ in enumerate(text):
        if pattern == text[index: (index + len(pattern))]:
            return index
    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    #Runtime: O(n), for same reasons as above. Array duplication is O(n), looping through the enumerated text is O(n), adding to O(2n) but ultimately being recorded and treated as O(n) because simplification is alright
    #Space: O(n). This is essentially the same code as the function above, EXCEPT that it returns an array rather than a single variable of constant size. We don't know how many times the pattern will be found; it could be one time, it could be a ton

    indices = []

    for index, _ in enumerate(text):
        if pattern == text[index: (index + len(pattern))]:
            indices.append(index)
    return indices


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
