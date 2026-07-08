def is_harshad(num):
    total = 0
    original_num = num
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    if original_num % total == 0 :
        return "Harshad"
    else:
        return "Not Harshad"
result = is_harshad(18)
print(result)