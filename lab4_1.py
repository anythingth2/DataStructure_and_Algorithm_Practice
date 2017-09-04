class Polynomial:
    def __init__(self,cofficient,power):
        self.cofficient = cofficient
        self.power = power
    
    def __str__(self):
        if self.power == 0:
            if self.cofficient > 0:
                return '+' + str(self.cofficient)
            elif self.cofficient == 0:
                return ''
            else:
                return str(self.cofficient)
        elif self.power == 1:
            if self.cofficient > 0:
                return '+' + str(self.cofficient) + 'n'
            elif self.cofficient == 0:
                return ''
            else:
                return str(self.cofficient)+'n'
        else:
            if self.cofficient > 0:
                return '+ ' + str(self.cofficient) + 'n^' + str(self.power)
            elif self.cofficient == 0:
                return ''
            else:
                return str(self.cofficient)+'n^'+str(self.power)

class Term:
    polynomial_seq = []
    def __init__(self,polynomial_seq):
        self.polynomial_seq = polynomial_seq
        self.sort()

    def add(self,poly):
        self.polynomial_seq.append(poly)
    
    def sort(self):
        self.polynomial_seq.sort(key= lambda x:x.power,reverse=True)

    def __add__(self,rhs):
        output = Term([])
        
        output.polynomial_seq = self.polynomial_seq + rhs.polynomial_seq
        for poly in output.polynomial_seq:
            for poly2 in output.polynomial_seq:
                if poly.power == poly2.power and poly is not poly2:
                    poly.cofficient += poly2.cofficient
                    output.polynomial_seq.remove(poly2)
        output.sort()
        return output

    def __str__(self):
        return ' '.join([ str(poly) for poly in self.polynomial_seq])

poly1 = Term( [Polynomial(3,95),Polynomial(1,7),Polynomial(10,4)] )
poly2 = Term( [Polynomial(21,100),Polynomial(-7,95),Polynomial(-2,4),Polynomial(15,3),Polynomial(4,2),Polynomial(-1,1), Polynomial(1,0)])

output = poly1 + poly2
print(output)
# print(x,y)
