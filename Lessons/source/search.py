#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)

def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found

#same as fxn above but + param saying 'start @ index 0'
#remember the card flipping activity. that third param = the extra info included when >1 person is flipping the cards
def linear_search_recursive(array, item, index=0):
    if index > len(array) - 1: #checks for index-range error
        return None
    elif array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)

def binary_search(array, item):
    """return the index of item in SORTED array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # CHANGE THIS to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item) #passes
    return binary_search_recursive(array, item) #also passes!

# Like doing it all by yourself. Oooh the WORK oooh the AGONY and STRESS
def binary_search_iterative(array, item):
    right = len(array)-1 #Set 'right' to rightmost index
    left = 0 #Set 'left' to leftmost index
    while right >= left: #Prevent from looking into already-discarded halves of array
        center = (right+left)//2 #Middle index of the sorted array
        center_target = array[center] #Actual content of aforementioned middle index
        if item == center_target: #Wow! A match! Return this lucky lotto winner
            return center
        elif item < center_target: #Less than center? Set 'right' to just left of the original middle
            right = center-1
        else: #elif item > center_target: #More than center? Set 'left' to just right of original middle
            left = center+1
    return None #never found item :(

# Like working with a cooperating, communicating team
# Card-flipping exercise from Class 2: Recursion & Search Algorithms (4.3.19)
# Flip over a card in the middle of a sorted list. No dice -> tell partner to look after or before
def binary_search_recursive(array, item, left=None, right=None):
    if right is None and left is None:
        right = len(array)-1 #Set 'right' to rightmost index by default
        left = 0 #Set 'left' to leftmost index by default
    elif right is None or left is None:
        raise AssertionError('Please specify either BOTH left and right params, or neither')
    # if right == None:
    #     right = len(array)-1 #Set 'right' to rightmost index by default
    # if left == None:
    #     left = 0 #Set 'left' to leftmost index by default
    center = (right+left)//2 #Middle index of the sorted array
    center_target = array[center] #Actual content of aforementioned middle index
    while right >= left: #Prevent from looking into already-discarded halves of array. FAILS w/o this
        if right > len(array) - 1 or left < 0: #Prevent wonky index nonsense.
            return None                  #May be unnecessary! Passes without this
        if item == center_target:
            return center
        elif item < center_target: #Less than center? Rerun fxn on array's left half. Ignore the right
            # return binary_search_recursive(array, item, left, center-1)
            right = center-1
            return binary_search_recursive(array, item, left, right)
        else: #elif item > center_target: #More than center? Rerun fxn on array's right half. Ignore the left
            # return binary_search_recursive(array, item, center+1, right)
            left = center+1
            return binary_search_recursive(array, item, left, right)

        return None
    return None




# Classmates' work presented in class


# def ikey_linear_search_recursive(array, item, index=0):
#     #Connor suggested: index == len(array) - 1, rather than >=
#     #This would be fine *for this specific case* because we increment by 1
#     #If we incremented by 2, 3, etc., >= would be critical
#     if index >= len(array): #checks for index-range error
#         return None
#     if array[index] == item: #if we find the item, stop recursing + return index
#         return index
#     return linear_search_recursive(array, item, index+1) #item not found, try next index
#     #Alan says: Why don't we pass in array[1:] for the first arg when running fxn again?
#     #B/c it's bad for recursive function calls because it costs time and memory
#     #Also it would be quadratic time, not linear time

# def jayce_binary_search_iterative(array, item):
#     #lmao 'roast me on my pseudocode'
#     #create a variable for the left and right boundaries
#     left_bound = 0 #left is the zero index of the array
#     right_bound = len(array)-1 #right is the full length of the array
#     # while left_bound <= current_middle_index and right_bound >= current_middle_index:
#     while left_bound <= right_bound: #code review: shortened from immediately above
#         current_middle_index = (left_bound + right_bound) // 2 #code review: moved into while loop
#         if array[current_middle_index] == item: #check that item is found and return index
#             return current_middle_index
#         elif array[current_middle_index] > item: #check that item is < or > current middle index value
#             right_bound = current_middle_index - 1
#         elif array[current_middle_index] < item:
#             left_bound = current_middle_index + 1
#         current_middle_index = (left_bound + right_bound) // 2
#     return None


# def faith_binary_search_recursive(array, item, left=None, right=None):
#     #first time thru, you have to set left and right val to span whole list
#     if left is None and right is None: #make sure that both or neither val is set
#         left = 0
#         right = len(array)-1
#     elif left is None or right is None: #one of these vals wasn't set
#         raise AssertionError('Please provide both left AND right, or neither')
    
#     midpoint = (left+right)//2 #keep track of middle value

#     if left > right: #base case 1, searched whole list
#         return None
#     if array[midpoint] == item: #base case 2, found item
#         return midpoint
#     #if item is larger than midpoint val, search right of midpoint
#     if array[midpoint] < item:
#         return binary_search_recursive(array, item, midpoint+1, right)
#     #item is smaller than midpoint val, search left of midpoint
#     return binary_search_recursive(array, item, left, midpoint-1)

# # Can we do what we write below?
# def faith_binary_search_recursive(array, item, left=0, right=len(array)-1)
# # NO. NO, WE CANNOT. Why???
# # When Python reads a line with 'def', it first reads the contents for syntax
# # Then it goes through the parameters and will set any default values one time
# # No context for it to say right=len(array)-1. That's why it's a big NO