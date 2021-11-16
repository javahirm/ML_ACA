first_row = "qwertyuiop" + "qwertyuiop".upper()
second_row = "asdfghjkl" + "asdfghjkl".upper()
third_row = "zxcvbnm" + "zxcvbnm".upper()


def one_line(word):
    word = set(word)
    length = len(word)
    counter = 0
    for elem in word:
        if elem in first_row:
            counter += 1
        elif elem in second_row:
            counter += 10
        else:
            counter += 100
    if counter in (length, length * 10, length * 100):
        return True
    else:
        return False


words = ["Hello", "Alaska", "Dad", "Peace", "omk", "qwerty", "sfd"]
words_one_liners = list(filter(one_line, words))
print(words_one_liners)
