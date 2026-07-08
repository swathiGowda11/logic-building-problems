def duck(num):
    while num > 0:
        digit = num % 10
        if digit == 0:
            return "duck"
        num //= 10
    return "not duck"
result = duck(1205)
print(result)

    