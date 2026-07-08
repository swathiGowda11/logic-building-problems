def binary_decimal(num):
    decimal = 0
    place = 1
    while num > 0:
        digit = num % 10
        decimal += digit * place
        place *= 2
        num //= 10
    return decimal
result = binary_decimal(1010)
print(result)
