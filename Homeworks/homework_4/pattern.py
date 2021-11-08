def is_pattern(pattern, word):
    dictionary_word_to_pattern = {}
    for x, y in zip(word, pattern):
        if x not in dictionary_word_to_pattern:
            dictionary_word_to_pattern[x] = y
    i = 0
    new_word = ""
    if len(dictionary_word_to_pattern.keys()) > len(set(dictionary_word_to_pattern.values())):
        return False
    else:
        while i < len(word):
            new_word += dictionary_word_to_pattern[word[i]]
            i += 1
        if new_word == pattern:
            return True
        else:
            return False


words = ["abab", "hjja", "gghd", "zzfc", "klll", "oopd"]
pattern = "eeri"
by_pattern = []
for word in words:
    if is_pattern(pattern, word) is True:
        by_pattern.append(word)

print(by_pattern)
