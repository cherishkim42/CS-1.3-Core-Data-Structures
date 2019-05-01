"""Search: 'python filter one list based on another' to solve"""

import string
import unittest
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual #kinda like method_override in npm

def test_blah():
    txt = ['I', 'like', 'to', 'eat', 'unhealthy', 'food', 'such', 'as', 'pizza', 'salad', 'and', 'popsicles']
    blocked = ['unhealthy', 'pizza', 'cake']
    assert redact_words(txt, blocked) == ['I', 'like', 'to', 'eat', 'food', 'such', 'as', 'salad', 'and', 'popsicles']

def redact_words(words, banned_words):
    censored_ver = []
    upper_bound = len(words) - 1
    i = 0 #initialize counter

    for word in words:
        while i <= upper_bound:
            if word != banned_words[i]:
                # censored_ver.append(word)
                i += 1
            censored_ver.append(word)
    return censored_ver
    #welp, Lucia explained why I was getting an index error
    #I'm using a counter based on WORDS array's length, to index in BANNED_WORDS array
    #ofc i'm getting an index error.. facepalm!!
    #thanks lucia!!

"""
Hooray pseudocode

Params: 2 arrays of strings
    1. the text
    2. the redacted words

Returns: array of words in array (1) that are NOT in (2)

1. Instantiate empty array
2. Lowercase contents of array (1) -- maybe later
3. For each word in array (1), IF that word is NOT in array (1), THEN add it to the empty array from STEP #1
4. Once each word from array (2) has been so checked, return the array from STEP #1

"""