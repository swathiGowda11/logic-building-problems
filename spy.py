def spy(num):
    product = 1
    total = 0
    while num > 0:
        digit = num % 10
        product *= digit
        total += digit
        num //= 10
    if product == total:
        return " spy"
    else:
        return " not spy"
result = spy(123)
print(result)