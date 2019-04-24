# from 
from set_hash import SetHash
import unittest
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class SetTest(unittest.TestCase):

    def test_init_v1(self): #❌ elements=None
        lilset = SetHash()
        assert len(lilset.hashet.buckets) == 8
        assert lilset.length() == 0
        assert lilset.size == 0

    def test_init_v2(self): #✅ elements!=None
        lilset = SetHash((('key1', 'value1'), ('key2', 'value2')))
        assert len(lilset.hashet.buckets) == 8
        assert lilset.length() == 2
        assert lilset.size == 2

    def test_add_and_get(self):
        lilset = SetHash()
        lilset.add(('hello', 'goodbye'))
        lilset.add(('sunny', 'inclement'))
        lilset.add(('full', 'hungry'))
        assert lilset.length() == 3
        assert lilset.size == 3
        lilset.add(('asoiaf', 'got'))
        assert lilset.get('hello') == 'goodbye'
        assert lilset.get('asoiaf') == 'got'
        assert lilset.length() == 4
        assert lilset.size == 4
 
    def test_contains(self):
        lilset = SetHash()
        lilset.add(('un', 1))
        lilset.add(('deux', 2))
        lilset.add(('trois', 3))
        assert lilset.contains(('un', 1)) is True
        assert lilset.contains(('deux', 2)) is True
        assert lilset.contains(('quatre', 4)) is False
        
    def test_remove(self):
        lilset = SetHash()
        lilset.add(('un', 1))
        lilset.add(('deux', 2))
        lilset.add(('trois', 3))
        lilset.add(('quatre', 4))
        assert lilset.length() == 4
        assert lilset.size == 4
        lilset.remove(('un', 1))
        assert lilset.length() == 3
        assert lilset.size == 3
        assert lilset.contains(('un', 1)) is False
        with self.assertRaises(KeyError): lilset.remove(('un', 1))
        with self.assertRaises(KeyError): lilset.remove(('two', 11))