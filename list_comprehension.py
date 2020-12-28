def identity(nums):
    """Identity:
    Given a list of numbers, write a list comprehension that produces a copy of the list.
        >>> identity([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]
        >>> identity([])
        []
    """
    lst = [a for a in nums]
    return lst
    #pass



def doubled(nums):
    """Doubled:
    Given a list of numbers, write a list comprehension that produces a list of each number doubled.
        >>> doubled([1, 2, 3, 4, 5])
        [2, 4, 6, 8, 10]
        >>> doubled([-2, 2, -10, 10])
        [-4, 4, -20, 20]
    """
    lst = [2*a for a in nums]
    return lst
    #pass
