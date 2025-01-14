'''
953. Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language
'''

# go thru again -> https://algo.monster/liteproblems/953

def isAlienSorted(words, order):

    h = {}

    for i in range(len(order)):
        h[order[i]] = i

    for i in range(20):
        previous_index = -1
        is_sorted_until_now = True

        for word in words:
            current_index = -1 if i >= len(word) else h[word[i]]

            if previous_index > current_index:
                return False

            if previous_index == current_index:
                is_sorted_until_now = False

            previous_index = current_index

        if is_sorted_until_now:
            return True

    return True


print(isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))


def isAlienSorted2(words, order):
  
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i+1]

        for j in range(len(word1)):
            # this handle scenarios where word2 is shorter but also a prefix of word1
            if j == len(word2):
                return False
            
            # if chars diffet check out their positions in the order
            elif word1[j] != word2[j]:
                if order.index(word1[j]) > order.index(word2[j]):
                    return False
                break
    return True
