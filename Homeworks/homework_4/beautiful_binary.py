def beautiful():
    n = int(input("Length of binary: "))
    b = input("Binary with n length: ")
    while True:
        if len(b) != n:
            b = input("Length is not n. Please input binary with length n: ")
        else:
            return b.count("010")


print(beautiful())
