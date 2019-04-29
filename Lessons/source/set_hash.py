from hashtable import HashTable
from linkedlist import LinkedList

class SetHash(object):
    
    def __init__(self, elements=None):
        """Initialize a new empty set structure 🍃 & add each element if a sequence is given."""
        self.hashet = HashTable() #hash + set = hashet
        self.size = 0 #num of key-val entries

        if elements is not None:
            for key, value in elements:
                new_element = (key, value)
                self.add(new_element)

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.hashet.buckets)

    def keys(self):
        all_keys = []
        for bucket in self.hashet.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def length(self):
        """Return the # of key-val entries by traversing buckets"""
        return self.hashet.length()
    
    def contains(self, element):
        """Return a boolean indicating whether 'element' is in this set."""
        index = self._bucket_index(element[0])
        bucket = self.hashet.buckets[index]
        #🐴hollyhock voice: idk, IS there an entry in this bucket with this key?
        entry = bucket.find(lambda key_value: key_value[0] == element[0])
        return entry is not None #returns T/F

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

    #🔥transformative method
    def add(self, element):
        """Add 'element' to this set, if not present already."""
        index = self._bucket_index(element[0])
        bucket = self.hashet.buckets[index]

        if self.contains(element) is True: #simplest base case
            raise KeyError('Have you forgotten? 😱 NO DUPLICATES! ❌👥❌ {} is already in this set!'.format(element))
        else:
            bucket.append(element)
            self.size += 1

    #🔥transformative method
    def remove(self, element):
        """Remove 'element' from this set, if present, or else raise KeyError"""
        index = self._bucket_index(element[0])
        bucket = self.hashet.buckets[index]

        if self.contains(element) is False: #simplest base case
            raise KeyError('Silly, you can\'t delete an element that isn\'t even in the set. I couldn\'t find {} anywhere. 😞'.format(element))
        else:
            bucket.delete(element) #calling on LL's delete method
            self.size -= 1

    #🌎generative method
    def union(self, other_set):
        """Return a new set that is the union of this and 'other_set', i.e. ALL elements w/ no dupes"""
        new_set = SetHash()

        if self.size > other_set.size:
            for element in other_set.hashet.keys():
                if self.contains(element):
                    if other_set.contains(element):
                        new_set.add(element)
        else:
            for element in self.hashet.keys():
                if other_set.contains(element):
                    if self.contains(element):
                        new_set.add(element)
        return new_set

    #🌎generative method
    def intersection(self, other_set):
        """Return a new set that is the intersection of this and 'other_set', i.e. OVERLAP elements"""
        new_set = SetHash()

        if self.size > other_set.size:
            for element in other_set.hashet.keys():
                if self.contains(element):
                    new_set.add(element)
        else:
            for element in self.hashet.keys():
                if other_set.contains(element):
                    new_set.add(element)
        return new_set

    #🌎generative method
    #NOTE: Whatever SELF has, that OTHER_SET does NOT
    def difference(self, other_set):
        """Return a new set that is the difference of this set and 'other_set'"""
        new_set = SetHash()

        for element in self.hashet.keys():
            if other_set.contains(element) is False:
                new_set.add(element)
        return new_set
    
    #🌎generative method
    def is_subset(self, other_set):
        """Return a boolean indicating whether 'other_set' is a subset of this set"""
        for element in other_set.hashet.keys():
            if self.contains(Element) is False:
                return False
        return True