# from 
from set_hash import SetHash
import unittest
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class SetTest(unittest.TestCase):

    def test_init_v1(self):
        lilset = SetHash()
        assert lilset.size == 0
        bts_diamond = SetHash(['taehyung', 'namjoon'])
        assert bts_diamond.length() == 2

    def test_contains(self):
        lilset = SetHash(['me!', 'look what you made me do', 'blank space', 'we are never ever getting back together'])
        assert lilset.length() == 4
        assert lilset.contains('me!') == True
        assert lilset.contains('red') == False
        assert lilset.contains('blank space') == True
        assert lilset.contains('love story') == False

    def test_add(self):
        lilset = SetHash()
        assert lilset.length() == 0
        lilset.add('zip')
        lilset.add('zap')
        assert lilset.contains('zip') == True
        assert lilset.contains('zap') == True
        assert lilset.contains('zop') == False
        lilset.add('zop')
        assert lilset.contains('zop') == True

    def test_remove(self):
        lilset = SetHash(['rice', 'bread', 'tortilla'])
        assert lilset.length() == 3
        lilset.remove('bread')
        assert lilset.length() == 2
        assert lilset.contains('bread') == False
        assert lilset.contains('rice') == True
        lilset.remove('tortilla')
        assert lilset.contains('tortilla') == False
        assert lilset.length() == 1

    def test_union(self):
        faves_set = SetHash(['namjoon', 'taehyung', 'seokjin'])
        rest_set = SetHash(['jimin', 'yoonggi', 'jungkook', 'hoseok'])
        union = faves_set.union(rest_set)
        assert union.size == 7
        assert union.contains('namjoon') == True
        assert union.contains('taehyung') == True
        assert union.contains('yoonggi') == True
        assert union.contains('sehun') == False

    def test_intersection(self):
        color_set = SetHash(['red', 'blue', 'pink', 'bed'])
        thing_set = SetHash(['book', 'desk', 'bed', 'pink'])
        intersection = color_set.intersection(thing_set)
        assert intersection.size == 2
        assert intersection.contains('red') == False
        assert intersection.contains('pink') == True

    def test_difference(self):
        fruit_set = SetHash(['apple', 'tomato', 'zucchini', 'peach'])
        veg_set = SetHash(['tomato', 'zucchini', 'celery'])
        difference = fruit_set.difference(veg_set)
        assert difference.size == 2
        assert difference.contains('apple') == True
        assert difference.contains('tomato') == False
        assert difference.contains('celery') == False

    def test_is_subset(self):
        best_stuff = SetHash(['sunrise', 'swimming', 'snuggling', 'reading', 'sleeping', 'sprinting', 'skating', 'taylor swift', 'writing', 'sketching'])
        s_words = SetHash(['sunrise', 'swimming', 'snuggling', 'sleeping', 'sprinting', 'skating', 'sketching'])
        assert best_stuff.is_subset(s_words) == True