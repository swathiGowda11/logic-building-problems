def is_neon(num):
    square = num * num
    total = 0
    while square > 0:
        digit = square % 10
        total += digit
        square //= 10
    return total == num

if __name__ == "__main__":
    num = 9
    print("Neon" if is_neon(num) else "Not neon")
