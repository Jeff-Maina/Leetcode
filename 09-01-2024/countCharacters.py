'''
1160. Find Words That Can Be Formed by Characters
Easy

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

'''

'''
removing an item mid list may cause issues to arise due to shifting indices
'''


def countCharacters(words, chars):
    h = {}

    temp = words.copy()

    for i in chars:
        if i not in h:
            h[i] = 1
        else:
            h[i] += 1

    for i in range(len(words)):
        word = words[i]

        for char in word:
            freq = word.count(char)

            if char not in h:
                temp.remove(word)
                break
            else:
                if freq > h[char]:
                    temp.remove(word)
                    break

    return sum([len(i) for i in temp])


print(countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))
