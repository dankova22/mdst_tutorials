"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if ((x % 2) == 1):
        return true
    else:
        return False

def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    for i in range (0, int(len(word)/2)):
        if word[i] != word[len(word) - i -1]:
            return False
    return True

def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    
    oddlist = []
    
    for i in numlist:
        if ( numlist[i] % 2 == 1):
            oddlist.append(numlist[i])
           
    return oddlist
            

def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    words = text.lower().split()
    dictionary = {}
    for word in words:
        dictionary[word] = 0
    for word in words;
        dictionary[word] +=1
    return dictionary
