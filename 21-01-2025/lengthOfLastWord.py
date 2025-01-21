def lengthOfLastWord(s):

    last_word = [word for word in s.split(" ") if word != ""][-1]

    return len(last_word)


print(lengthOfLastWord('   fly me   to   the moon  '))