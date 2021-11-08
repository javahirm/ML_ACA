s = input("Write something: ")
k = int(input("Integer: "))
length = len(s)
if k >= 0:
    print(s * k)
else:
    base = length / (-k)
    if base % base != 0:
        print("undefined")
    else:
        parts = [s[i: i + int(base)] for i in range(0, length, int(base))]
        first = parts[0]
        flag = True
        for elem in parts:
            if elem == first:
                flag = True
            else:
                flag = False
                break
        if flag is True:
            print(parts[0])
        else:
            print("undefined")
