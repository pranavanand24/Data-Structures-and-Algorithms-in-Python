def power0fTwo(n):
    if n == 0:
        return 1
    else:
        power = power0fTwo(n-1)
        return power * 2

print(power0fTwo(3))