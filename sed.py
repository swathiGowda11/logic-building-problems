def sum_of_even_digit(num):
    total = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            total += digit
        num = num // 10
    return total
result = sum_of_even_digit(48257)
print(result)
