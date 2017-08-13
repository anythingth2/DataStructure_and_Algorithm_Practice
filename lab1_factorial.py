def factorial(n):
    num = 1
    for i in range(n,1,-1):
        num*=i
    return num
    raise NotImplementedError()

print(factorial(9))