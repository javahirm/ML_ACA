def is_prime(number):
    for elem in range(2, int(number**0.5) + 1):
        if number % elem == 0:
            return False
    else:
        return True


n = int(input("Even integer > 2: "))
for elem in range(2, n):
    if is_prime(elem) is True and is_prime(n - elem) is True:
        print(elem, n - elem)
        break

