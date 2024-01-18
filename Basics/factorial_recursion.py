def factorial(num):
    if num == 1 or num == 0:
        return "---"
    
    return num * factorial(num - 1)

print(factorial(5))