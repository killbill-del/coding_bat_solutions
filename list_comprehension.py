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

    def squared(nums):
    """Squared:
    Given a list of numbers, write a list comprehension that produces a list of the squares of each number.
        >>> squared([1, 2, 3, 4, 5])
        [1, 4, 9, 16, 25]
        >>> squared([-2, 2, -10, 10])
        [4, 4, 100, 100]
    """
    lst = [a**2 for a in nums]
    return lst
    #pass



def evens(nums):
    """Evens:
    Given a list of numbers, write a list comprehension that produces a list of only the even numbers in that list.
        >>> evens([1, 2, 3, 4, 5])
        [2, 4]
        >>> evens([1, 3, 5])
        []
        >>> evens([-2, -4, -7])
        [-2, -4]
    """
    lst = [a for a in nums if a%2 == 0]
    return lst
    pass



def odds(nums):
    """Odds:
    Given a list of numbers, write a list comprehension that produces a list of only the odd numbers in that list.
        >>> odds([1, 2, 3, 4, 5])
        [1, 3, 5]
        >>> odds([2, 4, 6])
        []
        >>> odds([-2, -4, -7])
        [-7]
    """
    lst = [a for a in nums if a%2 != 0]
    return lst
    pass



def positives(nums):
    """Positives:
    Given a list of numbers, write a list comprehension that produces a list of only the positive numbers in that list.
        >>> positives([-2, -1, 0, 1, 2])
        [1, 2]
    """
    lst = [a for a in nums if a > 0]
    return lst
    pass



def selective_stringify_nums(nums):
    """Selectively stringify nums:
    Given a list of numbers, write a list comprehension that produces a list of strings of each number that is divisible by 5.
        >>> selective_stringify_nums([25, 91, 22, -7, -20])
        ['25', '-20']
    """
    lst = [str(a) for a in nums if a%5 ==0]
    return lst
    pass



def words_not_the(sentence):
    """Words not 'the'
    Given a sentence, produce a list of the lengths of each word in the sentence, but only if the word is not 'the'.
        >>> words_not_the('the quick brown fox jumps over the lazy dog')
        [5, 5, 3, 5, 4, 4, 3]
    """
    words = sentence.split()
    lst = [len(a) for a in words if str(a) != 'the']
    return lst
    pass



def vowels(word):
    """Vowels:
    Given a string representing a word, write a list comprehension that produces a list of all the vowels in that word.
        >>> vowels('mathematics')
        ['a', 'e', 'a', 'i']
    """
    lst = [w for w in word if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u']
    return lst
    pass



def vowels_set(word):
    """Vowels set:
    Given a string representing a word, write a set comprehension that produces a set of all the vowels in that word.
        >>> vowels_set('mathematics')
        set(['a', 'i', 'e'])
    """
    lst = set([w for w in word if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u'])
    return lst
    pass



def disemvowel(sentence):
    """Disemvowel:
    Given a sentence, return the sentence with all vowels removed.
        >>> disemvowel('the quick brown fox jumps over the lazy dog')
        'th qck brwn fx jmps vr th lzy dg'
    """
    vowels = ('a','e','i','o','u')
    for x in sentence:
        if x in vowels:
            sentence = sentence.replace(x,"")
    return sentence
    pass


def wiggle_numbers(nums):
    """Wiggle numbers:
    Given a list of number, return the list with all even numbers doubled, and all odd numbers turned negative.
        >>> wiggle_numbers([72, 26, 79, 70, 20, 68, 43, -71, 71, -2])
        [144, 52, -79, 140, 40, 136, -43, 71, -71, -4]
    """
    lst = []
    for x in nums:
        if x%2 == 0:
            x = 2*x
        elif x%2 !=0:
            x = -x
        lst.append(x)
    return lst
    pass



def encrypt_lol(sentence):
    """Encrypt lol:
    Given a sentence, return the setence will all it's letter transposed by 1 in the alphabet, but only if the letter is a-y.
        >>> encrypt_lol('the quick brown fox jumps over the lazy dog')
        'uif rvjdl cspxo gpy kvnqt pwfs uif mbzy eph'
    """
    #a = 'the quick brown fox jumps over the lazy dog'
    print(''.join([c if c == ' ' or ord(c) >= ord('y') else chr(ord(c) + 1) for c in sentence]))
    pass



# STOP HERE! You solved everything!
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print '\n*** ALL TESTS PASSED!\n'
