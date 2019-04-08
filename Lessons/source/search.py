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
    #If I try to stick this in a for loop (like above), it doesn't work
    if index > len(array) - 1:
        return None
    elif array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)

def binary_search(array, item):
    """return the index of item in SORTED array or None if item is not found"""
    # [CK] above emphasis mine
    # implement binary_search_iterative and binary_search_recursive below, then
    # CHANGE THIS to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item) #passes
    return binary_search_recursive(array, item) #hrmrhhrhmmm

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
    return None

# Like working with a cooperating, communicating team
# Card-flipping exercise from Class 2: Recursion & Search Algorithms (4.3.19)
# Flip over a card in the middle of a sorted list. No dice -> tell partner to look after or before
def binary_search_recursive(array, item, left=None, right=None):
    if right == None:
        right = len(array)-1 #Set 'right' to rightmost index by default
    if left == None:
        left = 0 #Set 'left' to leftmost index by default
    center = (right+left)//2 #Middle index of the sorted array
    center_target = array[center] #Actual content of aforementioned middle index
    while right >= left: #Prevent from looking into already-discarded halves of array. FAILS w/o this
        if right > len(array) - 1 or left < 0: #Prevent wonky index nonsense.
            return None                  #May be unnecessary! Passes without this
        if item == center_target: #Wow it matches? What're the odds. Return!
            return center
        elif item < center_target: #Less than center? Rerun fxn on array's left half. Ignore the right
            return binary_search_recursive(array, item, left, center-1)
        else: #elif item > center_target: #More than center? Rerun fxn on array's right half. Ignore the left
            return binary_search_recursive(array, item, center+1, right)
        return None
    return None