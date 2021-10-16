# SALARIES

# salary_1 = int(input("Salary: "))
# salary_2 = int(input("Salary: "))
# salary_3 = int(input("Salary: "))
#
# if salary_1 > salary_2 > salary_3:
#     print(salary_1 - salary_3)
# elif salary_1 > salary_3 > salary_2:
#     print(salary_1 - salary_2)
# elif salary_2 > salary_3 > salary_1:
#     print(salary_2 - salary_1)
# elif salary_2 > salary_1 > salary_3:
#     print(salary_2 - salary_3)
# elif salary_3 > salary_1 > salary_2:
#     print(salary_3 - salary_2)
# else:
#     print(salary_3 - salary_1)


# BORING NUMBERS


# def is_boring(number):
#     last_digit = number % 10
#     boring = True
#     while number > 0:
#         digit = number % 10
#         if digit != last_digit:
#             boring = False
#             break
#         number //= 10
#     return boring
#
#
# number = int(input())
# print('boring' if is_boring(number) is True else 'not boring')

# LARGEST NUMBER

# def largest_number(number):
#     while number > 9:
#         if number % 10 > number % 100 // 10:
#             return False
#         number //= 10
#     return True
#
#
# number = int(input("Number: "))
# print('No' if largest_number(number) else 'Yes')


# LINE SEGMENT INTERSECTION

# a1 = float(input("Number: "))
# b1 = float(input("Number: "))
# a2 = float(input("Number: "))
# b2 = float(input("Number: "))
#
# start_line2 = min(a2, b2)
# end_line2 = max(a2, b2)
# start_line1 = min(a1, b1)
# end_line1 = max(a1, b1)
#
# if a1 < start_line2 and b1 < start_line2:
#     print(0)
# elif a1 > end_line2 and b1 > end_line2:
#     print(0)
# elif start_line1 < a2 < end_line1 and start_line1 < b2 < end_line1:
#     print(abs(b2 - a2))
# else:
#     print(abs(end_line1 - start_line2))

# DIVISORS

number = int(input("Number: "))







