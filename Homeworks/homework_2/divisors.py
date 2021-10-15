def divisors(number):
    count = 2
    if number == 1:
        return 1
    else:
        for elem in range(2, int(number * 0.5) + 1):
            if number % elem == 0:
                count += 1
    return count


print(divisors(200))
