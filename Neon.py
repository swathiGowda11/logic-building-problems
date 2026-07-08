def neon(num):
    square = num * num
    total = 0
    while square > 0:
        digit = square % 10
        total += digit 
        square //= 10
    if total == num:
        return " Neon"
    else:
        return " Not Neon"
result = neon(9)
print(result)






'''solution2'''

num = 9
square = num * num
total = 0

while square > 0:
    digit = square % 10
    total += digit
    square //= 10

if total == num:
    print("Neon")
else:
    print("Not neon")
