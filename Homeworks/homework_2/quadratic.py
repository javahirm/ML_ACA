a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

D = b**2 - 4 * a * c
if a == 0 and b == 0 and c == 0:
    print("Non-quadratic equation")
    print("Infinite solutions")
elif a == 0 and b == 0 and c != 0:
    print("Non-quadratic equation")
    print("No solutions")
elif a == 0 and b != 0:
    print("Non-quadratic equation")
    print("One solution:", -c/b)
elif a != 0 and D < 0:
    print("Quadratic equation")
    print("Discriminant:", D)
    print("No solutions")
elif a != 0 and D == 0:
    print("Quadratic equation")
    print("Discriminant:", D)
    print("One solution:", -b/(2*a))
else:
    print("Quadratic equation")
    print("Discriminant:", D)
    print("Two solutions:", (-b + D**0.5)/ (2 * a), (-b - D**0.5)/ (2 * a))

