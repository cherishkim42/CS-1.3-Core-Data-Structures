"""Do Not Run - reference only!"""

# 💜04.24.19 set.py

# in Set class. Set __init__ fxn: .container -> hashtable, .size -> 0
def jamie_intersection(self, other_set):
    #Time complexity: O(n) or O(m), whichever one is smaller
    new_set = Set() #O(b) for # of buckets

    if self.size > other_set.size:
        #check to see which set is smaller and then iterate thru that one
        for element in other_set.container.keys(): #O(n)
            if self.contains(element): #O(1)
                new_set.add(element) #O(1)
    else:
        for element in self.container.keys(): #O(n)
            if other_set.contains(element): #O(1)
                new_set.add(element) #O(1)
    return new_set

def jamie_difference(self, other_set):
    new_set = Set()

    other_set_copy = other_set.copy.deepcopy() #to prevent transforming the original set

    for element in self.container.keys():
        #iterate thru the elements in .keys()
        if not other_set_copy.contains(element):
            new_set.add(element)
        else:
            other_set_copy.remove(element)

    return new_set

# 💜04.22.19 hashtable.py

def ali__resize(self, new_size=None):
    if new_size is None:
        new_size = len(self.buckets) * 2  # Double size
    elif new_size is 0:
        new_size = len(self.buckets) / 2  # Half size

    old_items = self.items() #old items in an array to hold all current key-val entries

    #alt to self.size = 0 & self.buckets = [LinkedList() for i in range(new_size)]
    self.__init__(new_size) #wipes out existing buckets and resets size
    #initiates a whole new set of buckets yeehaw im a cowgirl 🤠

    for key, value in old_items: #each entry is a lil linked list
        self.set(key, value) #inserts key-val entry into new list of buckets, which'll rehash based on the new size

# 💜04.15.19 linkedlist.py

def edwin_insert_at_index(self, index, item):
    if not (0 <= index < self.size): #Error if index out of range
        raise ValueError('List index out of range: {}'.format(index))
    #if index is first or last index, use append or prepend
    if index == 0:
        self.prepend(item)
        return
    if index == self.size:
        self.append(item)
        return
    node = self.head
    current_index = 0
    #loop thru LL while incr.'ing index. when index matches?!
    #set 'node' to new node with item and set node.next to none
    while node is not None:
        if current_index == index:
            prev_node = node
            current_node = node.next
            new_node = Node(item)
            new_node.next = current_node
            prev_node.next = new_node
            self.size += 1 #increment size for a node insertion
            return #once the job is done, this breaks out of the whole function
            # break #'break' would just exit the LOOP. nested loop -> breaks out of innermost loop
                #obviously doesn't break out of 'if' statements
        current_index += 1
        node = node.next

def dylan_replace(self, old_item, new_item):
    if self.tail.data == old_item: #check if old_item is in tail
        self.tail.data = new_item
        return
    
    curr = self.head #start at head
    while curr != None:
        if curr.data == old_item: #if the current node matches
            curr.data = new_item
            return
        curr = curr.next #climb
    # else: #can have ValueError in an 'else' if the while loop doesn't return or break. not rly needed
    #     raise ValueError('Value not found: {}'.format(old_item))
    raise ValueError('Value not found: {}'.format(old_item)) #not found, aka ELSE
    #like regifting a box! DATA swapped out, node 'container' kept.

# 💜04.08.19 search.py

def ikey_linear_search_recursive(array, item, index=0):
    #Connor suggested: index == len(array) - 1, rather than >=
    #This would be fine *for this specific case* because we increment by 1
    #If we incremented by 2, 3, etc., >= would be critical
    if index >= len(array): #checks for index-range error
        return None
    if array[index] == item: #if we find the item, stop recursing + return index
        return index
    return linear_search_recursive(array, item, index+1) #item not found, try next index
    #Alan says: Why don't we pass in array[1:] for the first arg when running fxn again?
    #B/c it's bad for recursive function calls because it costs time and memory
    #Also it would be quadratic time, not linear time

def jayce_binary_search_iterative(array, item):
    #lmao 'roast me on my pseudocode'
    #create a variable for the left and right boundaries
    left_bound = 0 #left is the zero index of the array
    right_bound = len(array)-1 #right is the full length of the array
    # while left_bound <= current_middle_index and right_bound >= current_middle_index:
    while left_bound <= right_bound: #code review: shortened from immediately above
        current_middle_index = (left_bound + right_bound) // 2 #code review: moved into while loop
        if array[current_middle_index] == item: #check that item is found and return index
            return current_middle_index
        elif array[current_middle_index] > item: #check that item is < or > current middle index value
            right_bound = current_middle_index - 1
        elif array[current_middle_index] < item:
            left_bound = current_middle_index + 1
        current_middle_index = (left_bound + right_bound) // 2
    return None

def faith_binary_search_recursive(array, item, left=None, right=None):
    #first time thru, you have to set left and right val to span whole list
    if left is None and right is None: #make sure that both or neither val is set
        left = 0
        right = len(array)-1
    elif left is None or right is None: #one of these vals wasn't set
        raise AssertionError('Please provide both left AND right, or neither')
    
    midpoint = (left+right)//2 #keep track of middle value

    if left > right: #base case 1, searched whole list
        return None
    if array[midpoint] == item: #base case 2, found item
        return midpoint
    #if item is larger than midpoint val, search right of midpoint
    if array[midpoint] < item:
        return binary_search_recursive(array, item, midpoint+1, right)
    #item is smaller than midpoint val, search left of midpoint
    return binary_search_recursive(array, item, left, midpoint-1)

# Can we do what we write below?
def faith_binary_search_recursive(array, item, left=0, right=len(array)-1)
# NO. 🙅🏻‍NO, WE CANNOT. 🙅🏻‍🙅🏻‍🙅🏻‍ WHY??? omg shes wearing purple i can't
# When Python reads a line with 'def', it first reads the contents for syntax
# Then it goes through the parameters and will set any default values one time
# No context for it to say right=len(array)-1. That's why it's a big NO


# 💜04.08.19: recursion.py

def jasmine_factorial_iterative(n):
    factorial = 1
    #2nd argument of RANGE is exclusive (not inclusive), tho the 1st is inclusive.
    #That's why it goes from 1 to n+1 - because that 2nd argument is exclusive!
    for i in range(1, n+1):
        print(factorial)
        factorial *= i
    return factorial


# 💜04.04.19: bases.py

def max_decode(digits, base): #Maximo's code review. Won't use. It's here for ref
    #suggested:
    #   - make 'alphabet' and 'digits' global-scope variables, as they'll likely be used by other fxns
    #   - validate that the digit even exists in the base passed in
    #       - ex. 'G' passed in with base 16 would return 16, not an error (as it should)
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base) #handle up to base36
    alphabet = string.ascii_lowercase
    digits = digits.lower() #make all lowercase for standardizing
    exponent = len(digits) - 1 #don't surpass what you're counting! This is the maximum power to which the base is taken
    num_result = 0 #instantiate

    for digit in digits:
        if digit.isnumeric(): #Alan's change
        # if digit not in alphabet: #check if digit is not a letter
            num_result += (base ** exponent) * int(digit) #'base**exponent' = 'pow(base, exponent)' in python
            # exponent -= 1
        elif digit in alphabet: #Alan's change
        # else: #if you get a letter
            hex_to_digit = ord(digit) - 87 #ORDinal: ascii char --> # that encodes it. The 87 is bc he lowercases all - if you don't lowercase it, you'll have a different number
            digit = hex_to_digit
            num_result += (base ** exponent) * int(digit)
            # exponent -= 1
        else:
            raise ValueError('...')
        exponent -= 1 #suggested change by classmate
    return num_result

def sukhrob_decode(number, base):
    dividend = number
    divisor = base
    quotient = 1
    result = ''
    while quotient != 0:
        if dividend < divisor: #if dividend < divisor, no need to divide. so dividend = remaidner
            remainder = dividend % divisor
            quotient = 0
        else:
            remainder = dividend % divisor
            dividend = (dividend - remainder) // divisor #updating the dividend until it's less than divisor
        
        if remainder > 9:
            #in ascii table, lowercase 'a' is at the number 97
            #so adding 10 + 87 = 97 => 'a', 11 + 87 = 98 => 'b' and so on
            remainder = chr(remainder + 87) #wow a magic number! Alan says set these equal to semantic variable names (ex. 'hex_letter_offset')

        result += str(remainder)

    return result[::-1] #flips the result at the end... because before return, result is in reverse order