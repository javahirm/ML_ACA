# Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/
# def good_pairs(nums):
#     dictionary = {}
#     for elem in nums:
#         if elem not in dictionary:
#             dictionary[elem] = 1
#         else:
#             dictionary[elem] += 1
#
#     pairs = 0
#     for key in dictionary:
#         if dictionary[key] > 1:
#             pairs += (dictionary[key] * (dictionary[key] - 1)) // 2
#
#     return pairs
#
#
# nums = [1,2,3]
# print(good_pairs(nums))

# Unique Number of Occurrences - https://leetcode.com/problems/unique-number-ofoccurrences/
# def unique_occurrences(arr):
#     dictionary = {}
#     for elem in arr:
#         if elem not in dictionary:
#             dictionary[elem] = 1
#         else:
#             dictionary[elem] += 1
#     list_occurrences = list(dictionary.values())
#     set_occurrences = set(list_occurrences)
#     if len(list_occurrences) == len(set_occurrences):
#         return True
#     else:
#         return False
#
#
# arr = [-3,0,1,-3,1,1,1,-3,10,0]
# print(unique_occurrences(arr))

# Distribute Candies - https://leetcode.com/problems/distribute-candies/
# def max_types(candyType):
#     list_types = []
#     for elem in candyType:
#         if elem not in list_types:
#             list_types.append(elem)
#     allowed = len(candyType)//2
#     types = len(list_types)
#     if allowed < types:
#         return allowed
#     else:
#         return types

# candyType = [6,6,6,6]
# print(max_types(candyType))


# Making Anagrams - https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
# a = "cde"
# b = "dcf"
#
# def anagrams(a, b):
#     counter = 0
#     for elem in a:
#         if elem not in b:
#             counter += 1
#     for elem in b:
#         if elem not in a:
#             counter += 1
#     return counter
#
# print(anagrams(a, b))

# Find Words Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
# def words_by_char(word, chars):
#     i = 0
#     while i < len(word):
#         flag = True
#         if word[i] not in chars:
#             flag = False
#             break
#         else:
#             chars = chars[:chars.index(word[i])] + chars[chars.index(word[i]) + 1:]
#         i += 1
#     if flag is True:
#         return True
#     else:
#         return False
#
#
# words = ["hello", "world", "leetcode"]
# chars = "welldonehoneyr"
#
# total_length = 0
# for word in words:
#     if words_by_char(word, chars) is True:
#         total_length += len(word)
#
# print(total_length)
#






