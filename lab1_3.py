def integer_right_triangle(p):
    triangle = []
    for a in range(1,p):
        for b in range(p-1,0,-1):
            c = (a**2 + b**2)**0.5
            if a+b+c == p:
                triangle.append((a,b,int(c)))
    return triangle[:len(triangle)//2]
    raise NotImplementedError()

print(integer_right_triangle(60))