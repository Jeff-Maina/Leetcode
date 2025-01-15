'''
2114. Maximum Number of Words Found in Sentences
Easy

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.
'''

# 3ms
def mostWordsFound(sentences):

    counts = [len(sentence.split(" ")) for sentence in sentences]

    return max(counts)


print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))