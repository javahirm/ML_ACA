def power_of_three(number):
    power = 1
    if number < 3:
        return 1
    else:
        while power < number:
            power *= 3
        return power // 3


print(power_of_three(10))
