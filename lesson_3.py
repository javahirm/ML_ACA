# INDEX SUM

# a = int(input("Length of sequence:" ))
# list_1 = []
# for i in range(a):
#     b = float(input("number: "))
#     list_1.append(b)
# c = int(input("Length of indices: "))
# list_2 = []
# for x in range(c):
#     d = int(input("Index: "))
#     list_2.append(d)
# i = 0
# sum_num = 0
# while i < len(list_2):
#     sum_num += list_1[list_2[i]]
#     i += 1
# print(sum_num)

# n = int(input("Length of list: "))
# numbers = []
#
# for elem in range(n):
#     numbers.append(float(input("Number: ")))
#
# m = int(input("Quantity of indices:"))
# indices = [int(input()) for elem in range(m)]
#
# s = 0
# for idx in indices:
#   s += numbers[idx]
#
# print(s)


# THE MOST DIVISOR RICH NUMBER


# def divisors(number):
#     count = 2
#     if number == 1:
#         return 1
#     else:
#         for elem in range(2, int(number * 0.5) + 1):
#             if number % elem == 0:
#                 count += 1
#     return count
#
#
# a = int(input("Number 1: "))
# b = int(input("Number 2: "))
#
# maximum = divisors(a)
# for elem in range(a, b + 1):
#     if divisors(elem) > divisors(maximum):
#         maximum = elem
# print(maximum)

# MONOTONICITY

# n = int(input("Quantity: "))
# numbers = [float(input()) for elem in range(n)]
#
# first = numbers[0]
# count = 0
# for elem in range(1, len(numbers)):
#     if numbers[elem] > first:
#         first = numbers[elem]
#         count += 1
#     else:
#         count -= 1
# if count == len(numbers) - 1:
#     print("ascending")
# elif count == -(len(numbers) - 1):
#     print("descending")
# else:
#     print("neither")

# list_1 = [1, 2, 3, 4, 5, 4, 400, 500, 4]
# maximum = list_1[0]
# for elem in range(len(list_1)):
#     if list_1[elem] > maximum:
#         maximum = list_1[elem]
# print(maximum)


# LUCKY NUMBERS

# n = int(input("int: "))
# sum_odd = 0
# sum_even = 0
# while n > 0:
#     sum_odd += n % 10
#     n //= 10
#     sum_even += n % 10
#     n //= 10
# if sum_odd == sum_even:
#     print("Lucky")
# else:
#     print("Not lucky")


# TREE

def sum_odd(number):
    sum_o = 0
    while number > 0:
        sum_o += number % 10
        number //= 100
    return sum_o


def sum_even(number):
    sum_ev = 0
    while number > 0:
        number //= 10
        sum_ev += number % 10
        number //= 100
    return sum_ev

print(sum_even(32323232))
print(sum_odd(323))



# for elem in range(n//2 + 1):
#     print(n//2 * " ", (n - n//2 - n // 2) * "*", n//2 * " ")



