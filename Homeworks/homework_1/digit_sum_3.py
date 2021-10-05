num = int(input("Please type a number: "))
sum_of_digits = num % 10 + num // 10 % 10 + num // 100
print(sum_of_digits)
