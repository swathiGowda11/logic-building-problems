def perfect_square(num):
    for i in range(1,num+1):
        if i*i == num:
            return "perfect square"
        
    return "Not perfect"
result = perfect_square(16)
print(result)