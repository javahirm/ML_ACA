# num = int(input("Please input a number: "))
# print(num % 10 + num//10 % 10 + num//100)

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# x = int(input("x: "))
# print(a*(x**2)+(b*x)+c)

# num = float(input("Input a float positive number: "))
# print(int(num*2 -int(num)))

# a = input()
# b = input()
#
# print("Initial value of a", a)
# print("Initial value of b", b)
#
# c = a
# a = b
# b = c
#
# print("Swapped value of a", a)
# print("Swapped value of b", b)

# possible_colors = int(input("N: "))
# print(possible_colors + 1)

n = int(input("n: "))
an = int(input("an: "))
m = int(input("m: "))
am = int(input("am: "))
k = int(input("k: "))
d = (an - am)/(n-m)
a1 = an - ((n-1)*d)
print(a1 + ((k-1)*d))
