def count_odd_dig(num):
    count = 0
    while num > 0:
        digit = num % 10
        if digit % 2 != 0:
            count += 1
        num = num // 10
    return count
result = count_odd_dig(48257)
print(result)
