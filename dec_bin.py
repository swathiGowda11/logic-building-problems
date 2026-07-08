def decimal_binary(num):
    binary = 0
    place = 1
    while num > 0:
        remainder = num % 2
        binary += remainder * place
        place *= 10
        num //= 2
    return binary
result = decimal_binary(10)
print(result)