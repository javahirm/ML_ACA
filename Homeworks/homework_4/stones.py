jewels = input("jewels: ")
stones = input("stones: ")
count = 0
for elem in stones:
    if elem in jewels:
        count += 1
print(count)
