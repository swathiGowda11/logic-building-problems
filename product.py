def product_of_digits(num):
    product = 1
    while num > 0:
        digit = num % 10
        product *= digit
        num = num // 10
    return product
result = product_of_digits(234)
print(result)