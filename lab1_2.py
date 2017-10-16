def multiples_of_3_and_5(n):
    num = 0
    for i in range(n):
        if i%3 == 0 or i%5 == 0:
            num+=i
    return num
    raise NotImplementedError()

def multiples_of_3_and_5_new(n):
    return sum([i for i in range(10) if i%3 == 0 or i%5 == 0])

# print(multiples_of_3_and_5(10))