def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


print(factorial(7) // factorial(3) // factorial(4))