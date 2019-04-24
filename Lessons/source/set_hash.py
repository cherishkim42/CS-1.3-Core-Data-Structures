"""
I've elected to build this set class with... drumroll please... a HASH TABLE!

Presuppositions of this class:
* "elements" parameter always passed in as (key, value) pair
* The correct approach to the above is to split elements into explicitly defined variables for the key and the value and then use the key to go hunt
* Currently unsure of other ways, aside from the obvious passing in of just a key

Remaining:
* union(other_set): return a new set that is the union of this and ~other_set~
* intersection(other_set): return a new set that is the intersection of this set and ~other_set~
* is_subset(other_set): return a boolean indicating whether ~other_set~ is a subset of this set
"""

from hashtable import HashTable
from linkedlist import LinkedList

class SetHash(object):
    
    def __init__(self, elements=None):
        """Initialize a new empty set structure 🍃 & add each element if a sequence is given."""
        self.hashet = HashTable()
        self.size = 0 #num of key-val entries

        if elements is not None:
            for key, value in elements:
                new_element = (key, value)
                self.add(new_element)

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.hashet.buckets)

    def length(self):
        """Return the # of key-val entries by traversing buckets"""
        return self.hashet.length()
    
    def contains(self, element):
        """Return a boolean indicating whether 'element' is in this set."""
        index = self._bucket_index(element[0])
        bucket = self.hashet.buckets[index]
        #🐴hollyhock voice: idk, IS there an entry in this bucket with this key?
        entry = bucket.find(lambda key_value: key_value[0] == element[0])
        if entry is not None:
            return True
        else:
            return False

    def get(self, key):
        """Return the value associated with the given key, or raised KeyError."""
        index = self._bucket_index(key)
        bucket = self.hashet.buckets[index]
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:
            raise KeyError('I can\'t retrieve something that\'s not there! \'{}\' not found 😭'.format(key))

    def add(self, element):
        """Add 'element' to this set, if not present already."""
        index = self._bucket_index(element[0])
        bucket = self.hashet.buckets[index]

        if self.contains(element) is True: #simplest base case
            raise KeyError('Have you forgotten? 😱 NO DUPLICATES! ❌👥❌ {} is already in this set!'.format(element))
        else:
            bucket.append(element)
            self.size += 1

    def remove(self, element):
        """Remove 'element' from this set, if present, or else raise KeyError"""
        index = self._bucket_index(element[0])
        bucket = self.hashet.buckets[index]

        if self.contains(element) is False: #simplest base case
            raise KeyError('Silly, you can\'t delete an element that isn\'t even in the set. I couldn\'t find {} anywhere. 😞'.format(element))
        else:
            bucket.delete(element) #calling on LL's delete method
            self.size -= 1