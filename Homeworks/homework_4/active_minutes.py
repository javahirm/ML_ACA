logs = [[1, 1], [2, 2], [2, 3]]
k = 4

dictionary = {}
for log in logs:
    if log[0] not in dictionary:
        dictionary[log[0]] = [log[1]]
    else:
        dictionary[log[0]].append(log[1])

list_of_uam = []
for values in dictionary.values():
    list_of_uam.append(len(set(values)))

final_list = k * [0]
i = 0
while i < k:
    if i in list_of_uam:
        final_list[i-1] = list_of_uam.count(i)
    i += 1

print(final_list)
