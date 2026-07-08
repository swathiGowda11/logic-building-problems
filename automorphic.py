def automorphic(num):
    count = 0
    original_num = num 
    while num > 0:
        count += 1
        num = num // 10
    square = original_num * original_num
    last_digits = square % (10 ** count)
    if last_digits == original_num:
        return "Automorphic"
    else:
        return "Not Automorphic"
result = automorphic(25)
print(result)


