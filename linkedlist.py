class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = self.tail = None
    
    def __str__(self):
        output =''
        n = self.head
        while n is not self.tail:
            output += ' ' + str(n.data)
            n = n.next
        output+=' ' + str(n.data)
        return output
    def append(self,data):
        if self.head == None:
            self.head = node(data)
            self.tail = self.head
        else:
            tail = self.tail
            tail.next = node(data)
            self.tail = tail.next
x = linkedlist()
x.append('a')
x.append('b')
x.append('c')
print(x)
