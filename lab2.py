def multiples_of_3_and_5(n):
    num = 0
    for i in range(n):
        if i%3 == 0 or i%5 == 0:
            num+=i
    return num
    raise NotImplementedError()

print(multiples_of_3_and_5(10))