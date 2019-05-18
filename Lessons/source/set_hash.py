from hashtable import HashTable

class SetHash(object):
    
    def __init__(self, elements=None):
        self.hashet = HashTable() #hash + set = hashet
        self.size = 0 #num of key-val entries

        if elements is not None:
            for element in elements:
                self.add(element)

    def __iter__(self):
        for item in self.all_items():
            yield item

    def all_items(self):
        return self.hashet.keys()
    
    def contains(self, key):
        return self.hashet.contains(key)

    def length(self):
        return self.size

    def add(self, element):
        self.size += 1
        return self.hashet.set(element, element)

    def remove(self, element):
        self.size -= 1
        return self.hashet.delete(element)

    def union(self, other_set):
        """Return a new set that is the union of this and 'other_set', i.e. ALL elements w/ no dupes"""
        union = other_set
        for item in self:
            union.add(item)
        return union

    def intersection(self, other_set):
        """Return a new set that is the intersection of this and 'other_set', i.e. OVERLAP elements"""
        intersection = SetHash()

        if other_set.size < self.size:
            smaller_set = other_set
            larger_set = self
        else:
            smaller_set = self
            larger_set = other_set
        for item in smaller_set:
            if larger_set.contains(item):
                intersection.add(item)
        return intersection

    #NOTE: Whatever SELF has, that OTHER_SET does NOT
    def difference(self, other_set):
        """Return a new set that is the difference of this set and 'other_set'"""
        difference = self
        intersection = self.intersection(other_set)

        for item in intersection:
            difference.remove(item)
        return difference
    
    def is_subset(self, other_set):
        """Return a boolean indicating whether 'other_set' is a subset of this set"""
        if other_set.size > self.size:
            return False
        for item in other_set:
            if not self.contains(item):
                return False
        return True