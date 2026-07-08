def is_disarium(num):
    original = num
    count = 0
    temp = num

    if temp == 0:
        count = 1
    while temp > 0: 
        temp //= 10
        count += 1

    temp = original
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** count
        count -= 1
        temp //= 10

    return total == original


def main():
    number = 135
    if is_disarium(number):
        print(f"{number} is a Disarium number")
    else:
        print(f"{number} is not a Disarium number")


if __name__ == "__main__":
    main()

