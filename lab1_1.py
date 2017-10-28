def factorial(n):
    num = 1
    for i in range(n,1,-1):
        num*=i
    return num
    raise NotImplementedError()

factorial2 = lambda x: x * factorial2(x - 1) if x else 1

# print(factorial(9))