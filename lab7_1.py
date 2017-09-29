def printNdown(n):
    if n==1:
        print(n,end=' ')
    else:
        print(n)
        printNdown(n-1)

def printToN(n):
    if n==1:
        print(n ,end= ' ')
    else:
        printToN(n-1)
        print(n,end=' ')

def sumToN(n):
    if n==1:
        return 1
    else: 
        return n+sumToN(n-1)

def printForw(lists):
    if len(lists) != 0:
        return str(lists.pop(0)) + str(printForw(lists))
    else:return ''

def printBack(lists):
    if len(lists) != 0:
        return str(lists.pop()) + str(printBack(lists))
    else:return ''

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return self.data

class lists:
    def __init__(self,lists_head = None):
        if lists_head == None:
            self.head = self.tail = None
        else:
            self.head = node(lists_head.pop(0))
            n = self.head
            while len(lists_head) != 0:
                n.next = node(lists_head.pop(0))
                self.tail = n
                n = n.next
            
    def __str__(self):
        output = ''
        n = self.head
        while n.next != None:
            print(n.data,end=' ')
            n = n.next
        print(n.data)
        return ''

def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(20))
x = lists([1,2,3,4,5])

#print(x)


#printNdown(5)
#printToN(5)
#print(sumToN(10))
#print(printForw([1,2,3,4,5]))
#print(printBack([1,2,3,4,5]))
