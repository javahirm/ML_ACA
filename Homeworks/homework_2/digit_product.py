def digit_product(number):
    product = 1
    while number > 0:
        digit = number % 10
        if digit != 0:
            product = product * digit
        number //= 10
    return product


print(digit_product(23456))



