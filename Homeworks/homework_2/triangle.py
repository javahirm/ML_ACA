def triangle(a, b, c):
    if c >= a + b or b >= a + c or a >= b + c:
        return "No Triangle"
    elif c**2 == a**2 + b**2 or b**2 == a**2 + c**2 or a**2 == c**2 + b**2:
        return "Right Triangle"
    elif c**2 > a**2 + b**2 or b**2 > a**2 + c**2 or a**2 > c**2 + b**2:
        return "Obtuse Triangle"
    elif c**2 < a**2 + b**2 or b**2 < a**2 + c**2 or a**2 < c**2 + b**2:
        return "Acute Triangle"


print(triangle(4, 4, 4))
