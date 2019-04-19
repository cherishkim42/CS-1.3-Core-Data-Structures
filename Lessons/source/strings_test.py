#!python

from strings import contains, find_index, find_all_indexes
import unittest


class StringsTest(unittest.TestCase):

    def test_contains_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert contains('abc', '') is True  # all strings contain empty string
        assert contains('abc', 'a') is True  # single letters are easy
        assert contains('abc', 'b') is True
        assert contains('abc', 'c') is True
        assert contains('abc', 'ab') is True  # multiple letters are harder
        assert contains('abc', 'bc') is True
        assert contains('abc', 'abc') is True  # all strings contain themselves
        assert contains('aaa', 'a') is True  # multiple occurrences
        assert contains('aaa', 'aa') is True  # overlapping pattern
        # TODO: Write more positive test cases with assert is True statements
        # ...
        assert contains('bookshelf', 'book') is True
        assert contains('marymoocow', 'cow') is True
        assert contains('marymoocow', 'moo') is True
        assert contains('abcdefg', 'def') is True

    def test_contains_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert contains('abc', 'z') is False  # remember to test other letters
        assert contains('abc', 'ac') is False  # important to test close cases
        assert contains('abc', 'az') is False  # first letter, but not last
        assert contains('abc', 'abz') is False  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is False statements
        # ...
        assert contains('bookshelf', 'no books') is False
        assert contains('wackadoodledoo', 'abc') is False
        assert contains('1234456131343141322222ab', 'qr') is False
        assert contains('!!!!!!!!!!', 'abcdefg') is False

    def test_contains_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert contains('ababc', 'ab') is True  # multiple occurrences
        assert contains('banana', 'na') is True  # multiple occurrences
        assert contains('ababc', 'abc') is True  # overlapping prefix
        assert contains('bananas', 'nas') is True  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        assert contains('Long live all the mountains we moved', 'we') is True
        assert contains('its delicate', 'deli') is True
        assert contains('shooby doo bap bap', 'o bap') is True
        assert contains('housemate', 'house') is True

    def test_find_index_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_index('abc', '') == 0  # all strings contain empty string
        assert find_index('abc', 'a') == 0  # single letters are easy
        assert find_index('abc', 'b') == 1
        assert find_index('abc', 'c') == 2
        assert find_index('abc', 'ab') == 0  # multiple letters are harder
        assert find_index('abc', 'bc') == 1
        assert find_index('abc', 'abc') == 0  # all strings contain themselves
        assert find_index('aaa', 'a') == 0  # multiple occurrences
        assert find_index('aaa', 'aa') == 0  # overlapping pattern
        # TODO: Write more positive test cases with assert equal int statements
        # ...
        assert find_index('aldjg', 'g') == 4
        assert find_index('abcdefghijklmnop', 'a') == 0
        assert find_index('woooooop', 'oop') == 5
        assert find_index('Ice Cream and Gelato are not synonymous', 'mous') == 35
        assert find_index('literally different recipes', 'different recipes') == 10

    def test_find_index_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_index('abc', 'z') is None  # remember to test other letters
        assert find_index('abc', 'ac') is None  # important to test close cases
        assert find_index('abc', 'az') is None  # first letter, but not last
        assert find_index('abc', 'abz') is None  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is None statements
        # ...
        assert find_index('the bible', 'PICKLE RIIIIIICK') is None
        assert find_index('your honor that is wonderful', 'your honor with all due respect that is bogus') is None
        assert find_index('meow', 'me_irl') is None
        assert find_index('dangerous gateway properties', 'trees') is None
        assert find_index('safest way to have fun!', 'crack') is None
        assert find_index('these are not supposed to be jokes its just easier to make them not match when i put in absurd things', 'dont you like playing volleyball when its negative 10 degrees and you left your favorite coat in Korea') is None

    def test_find_index_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_index('ababc', 'abc') == 2  # overlapping prefix
        assert find_index('bananas', 'nas') == 4  # overlapping prefix
        assert find_index('abcabcabc', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcab', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcdef', 'abcd') == 3  # overlapping prefix
        assert find_index('abcabcdef', 'abcdef') == 3  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcde') == 7  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcd') == 3  # multiple occurrences, overlapping prefix
        assert find_index('abra cadabra', 'abra') == 0  # multiple occurrences
        assert find_index('abra cadabra', 'adab') == 6  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        # ...
        assert find_index('~the bridge is crossed so staaaaand and watch it buuuuuuuurnnnnn', 'the') == 1
        assert find_index('cock-a-doodle-doo im a rooster', 'doodle') == 7
        assert find_index('xyxyxyxyxyxyxyxyxyz', 'xyxyxyxyxy') == 0
        assert find_index('magic and mystery', 'and mys') == 6

    def test_find_all_indexes_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_all_indexes('abc', '') == [0, 1, 2]  # all strings contain empty string
        assert find_all_indexes('abc', 'a') == [0]  # single letters are easy
        assert find_all_indexes('abc', 'b') == [1]
        assert find_all_indexes('abc', 'c') == [2]
        assert find_all_indexes('abc', 'ab') == [0]  # multiple letters are harder
        assert find_all_indexes('abc', 'bc') == [1]
        assert find_all_indexes('abc', 'abc') == [0]  # all strings contain themselves
        assert find_all_indexes('aaa', 'a') == [0, 1, 2]  # multiple occurrences
        assert find_all_indexes('aaa', 'aa') == [0, 1]  # overlapping pattern
        # TODO: Write more positive test cases with assert equal list statements
        # ...
        assert find_all_indexes('umbrella ella', 'ella') == [4, 9]
        assert find_all_indexes('mississippi', 'ss') == [2, 5]
        assert find_all_indexes('minimum', 'm') == [0, 4, 6]
        assert find_all_indexes('quality quest', 'qu') == [0, 8]
        assert find_all_indexes('quality quidditch supplies', 'i') == [4, 10, 13, 23]

    def test_find_all_indexes_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_all_indexes('abc', 'z') == []  # remember to test other letters
        assert find_all_indexes('abc', 'ac') == []  # important to test close cases
        assert find_all_indexes('abc', 'az') == []  # first letter, but not last
        assert find_all_indexes('abc', 'abz') == []  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert equal list statements
        # ...
        assert find_all_indexes('baby baby i feel crazy', 'i feel so sane this is a healthy relationship') == []
        assert find_all_indexes('dear scammer clairvoyant will i marry my celebrity crush', 'uhh no but im gonna tell you what you wanna hear') == []
        assert find_all_indexes('some canonical text', 'cherry-picked ideas') == []
        assert find_all_indexes('objective reality', 'innately biased lens') == []
        assert find_all_indexes('aaaaaaaaaaaaaaaaaa', 'zymnop') == []

    def test_find_all_indexes_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_all_indexes('ababc', 'abc') == [2]  # overlapping prefix
        assert find_all_indexes('bananas', 'nas') == [4]  # overlapping prefix
        assert find_all_indexes('abcabcabc', 'abc') == [0, 3, 6]  # multiple occurrences
        assert find_all_indexes('abcabcab', 'abc') == [0, 3]  # multiple occurrences
        assert find_all_indexes('abcabcdef', 'abcd') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdef', 'abcdef') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcde') == [7]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcd') == [3, 7]  # multiple occurrences, overlapping prefix
        assert find_all_indexes('abra cadabra', 'abra') == [0, 8]  # multiple occurrences
        assert find_all_indexes('abra cadabra', 'adab') == [6]  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        # ...
        assert find_all_indexes('babo gataseo', 'babo') == [0]
        assert find_all_indexes('who are you anyway', 'a') == [4, 12, 16]
        assert find_all_indexes('tell me why why why oh', 'why') == [8, 12, 16]
        assert find_all_indexes('tear bear ear canal', 'ear') == [1, 6, 10]
        assert find_all_indexes('burrito perro guerra', 'rr') == [2, 10, 17]
        assert find_all_indexes('isnt it isnt it isnt it', 'isnt it') == [0, 8, 16] #taylor swift! ♥
        assert find_all_indexes('sandbox andromeda and androgyny', 'and') == [1, 8, 18, 22]
        assert find_all_indexes('immunology biology otolaryngology etymology mythology', 'ology') == [5, 13, 28, 38, 48]





if __name__ == '__main__':
    unittest.main()
