from set_hash import SetHash
import unittest
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

"""contains ➕ add ➕ remove"""

class SetTest(unittest.TestCase):

    def test_init_v1(self): #❌ passing in elements
        lil_set = SetHash(10)
        assert len(hashy.buckets) == 10
        assert hashy.length() == 0
        assert hashy.size == 0

    def test_init_v2(self): #✅ passing in elements

    def test_contains(self):
        hashy = SetHash()
