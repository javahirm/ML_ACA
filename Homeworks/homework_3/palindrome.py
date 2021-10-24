def is_palindrome(number):
    initial = number
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10
    if initial == reverse:
        return True
    else:
        return False


a = int(input("a: "))
b = int(input("b: "))

for elem in range(a, b + 1):
    if is_palindrome(elem) is True:
        print(elem)
