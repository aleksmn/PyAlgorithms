'''
Given a string of words, reverse all the words
'''

def reverse(s):
    s = s.split()
    s.reverse()
    return ' '.join(s)

def reverse2(s):
    return ' '.join(s.split()[::-1])

def reverse3(s):

    length = len(s)
    spaces = [' ']
    words = []
    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i])

        i += 1

    return " ".join(reversed(words))

print(reverse3('Hello there'))
