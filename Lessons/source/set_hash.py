"""
NONE OF THIS IS TESTED IN ANY WAY pls for your own good don't use as reference

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

#must pass in key-val pairs for elements in the form (key, val)

from linkedlist import LinkedList

class SetHash(object):
    
    def __init__(self, init_size=8, elements=None):
        """Initialize a new empty set structure 🍃 & add each element if a sequence is given."""
        # super(Set, self).__init__() #❌calling Set's parent class❌
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0 #num of key-val entries

        if elements is not None:
            for key, value in elements:
                new_element = (key, value)
                self.add(new_element)

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def length(self):
        """Return the # of key-val entries by traversing buckets"""
        #straight-up taken from hashtable.py
        return sum(bucket.length() for bucket in self.buckets)
    
    def contains(self, element):
        """Return a boolean indicating whether 'element' is in this set."""
        element_key = []
        for slot in self.buckets:
            for key, value in slot.items():
                element_key.append[key]
        index = self._bucket_index(element_key[0]) #first and only element of element_key is at index 0
        bucket = self.buckets[index]
        #🐴hollyhock voice: idk, IS there an entry in this bucket with this key?
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None #returns T/F

    def add(self, element):
        """Add 'element' to this set, if not present already."""
        # key = key_element_helper(element)
        # val = val_element_helper(element)
        # index = self._bucket_index(target_key[0])
        # bucket = self.buckets[index]

        if self.contains(element) is True: #simplest base case
            raise KeyError('Have you forgotten? 😱 NO DUPLICATES! ❌👥❌ {} is already in this set!'.format(element))
        else:
            bucket.append(element)
            self.size += 1

    def remove(self, element):
        """Remove 'element' from this set, if present, or else raise KeyError"""
        # key = key_element_helper(element)
        # val = val_element_helper(element)
        # index = self._bucket_index(target_key[0])
        # bucket = self.buckets[index]

        if self.contains(element) is False: #simplest base case
            raise KeyError('Silly, you can\'t delete an element that isn\'t even in the set. I couldn\'t find {} anywhere. 😞'.format(element))
        else:
            bucket.delete(element) #calling on LL's delete method
            self.size -= 1


    # #unneeded helper functions
    # def key_element_helper(self, element):
    #     """Hooray DRYness"""
    #     element_key = []
    #     for slot in self.buckets:
    #         for key, value in slot.items():
    #             element_key.append[key]
    #     return element_key

    # def val_element_helper(self, element):
    #     """yeah lol idk when you would ever use this"""
    #     element_val = []
    #     for slot in self.buckets:
    #         for key, value in slot.items():
    #             element_val.append[value]
    #     return element_val