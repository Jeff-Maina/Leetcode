'''

1736. Latest Time by Replacing Hidden Digits
Easy
Topics
Companies
Hint
You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

'''


# def maximumTime(time):
#     h, m = time.split(':')

#     i1 = h.index("?")
#     m1 = m.index("?")

#     if i1 == 1:
#         if int(h[0]) < 2:
#             h = h.replace("?", "9")
#         else:
#             h = h.replace("?", "3")
#     else:
#         if int(h[1]) < 4:
#             h = h.replace("?", "2")
#         else:
#             h = h.replace("?", "1")

#     if m1 == 0:
#         m = m.replace("?", "5")
#     else:
#         m = m.replace("?", "9")

# return ":".join([h, m])


def maximumTime(time):

    h, m = time.split(":")

    if "?" in h:
        indices = [i for i, c in enumerate(h) if c == "?"]

        if len(indices) > 1:
            h = "24"
        else:
            if indices[0] == 0:
                h = h.replace("?", "2") if int(
                    h[1]) < 4 else h.replace("?", "1")

            if indices[0] == 1:
                h = h.replace("?", "9") if int(
                    h[0]) < 2 else h.replace("?", "3")

    if "?" in m:
        indices = [i for i, c in enumerate(m) if c == "?"]

        if len(indices) > 1:
            m = "59"
        else:
            if indices[0] == 0:
                m = m.replace("?", "5")
            else:
                m = m.replace("?", "9")

    return ":".join([h, m])


print(maximumTime("2?:?0"))
