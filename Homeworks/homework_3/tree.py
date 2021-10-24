base = int(input("Odd number: "))
for elem in reversed(range(0, base // 2 + 1)):
    print(elem * " ", (base - 2 * elem) * "*", elem * " ")
