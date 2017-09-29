class node:
    def __init__(self,data,nexts = None):
        self.data = data
        self.nexts = nexts 

    def __str__(self):
        return self.data

class List:

    def __init__(self,data = None):
        self.head = self.tail = node(data)
        self.size = 0 if data == None else 1
    def __str__(self):
        p = self.head
        while p.nexts != None:
            print(p.data,end=' ')
            p = p.nexts
        print(p.data)
        return ''
    
    def isEmpty(self):
        return self.size == 0

    def append(self,data):
        p = node(data)
        if self.head.data == None:
            self.head = p
            self.tail = self.head
        self.tail.nexts = p
        self.tail = p
        self.size += 1
    
    def addHead(self,data):
        p = node(data,self.head)
        self.head = p
        self.size +=1

    def isIn(self,data):
        t = self.head
        while t.nexts != None:
            if t.data == data:
                return True
            t = t.nexts
        if t.data == data:
            return True
        return False

    def before(self,data):
        before = None
        i = self.head
        while i.nexts != None:
            if i.data == data:
                return before
            before = i
            i = i.nexts
        if i.data == data:
            return before
        return None

    # def remove(self,data):
    #     if not self.isIn(data) or self.before(data) == None:
    #         print('Failed to remove')
    #         return
    #     self.before(data).nexts = self.before(data).nexts.nexts
    
    def remove(self,index):
        currentNode = self.get(index-1)
        currentNode.nexts= self.get(index+1)
    def removeTail(self):
        t = self.before(self.tail.data)
        t.nexts = None
        self.tail = t

    def removeHead(self):
        self.head = self.head.nexts

    def get(self,index):
        if index > self.size:
            raise IndexError
        t = self.head
        for i in range(index):
            t = t.nexts
        if t != None:
            return t

    def insert(self,node,index):
        currentNode = self.get(index)
        nextNode = currentNode.nexts
        
        currentNode.nexts = node
        node.nexts = nextNode

        
class Poke(List):
    def __init__(self,start,end):
        List.__init__(self,)
        for i in range(start,end+1):List.append(self,str(i))
    def bottomUp(self,factor):
        if factor <= 0 or factor >= 1:
            raise IOError('factor must in range 0 - 1')
        sizeBottomUp =int(self.size*factor)
        newTail = self.get(sizeBottomUp)
        newHead = newTail.nexts
        oldHead = self.head
        oldTail = self.tail
        oldTail.nexts = oldHead
        self.tail = newTail
        self.tail.nexts = None
        self.head = newHead
    def deBottomUp(self,factor):
        if factor <= 0 or factor >= 1:
            raise IOError('factor must in range 0 - 1')
        sizeDeBottomUp = int(self.size*factor)
        newTail = self.get(self.size - sizeDeBottomUp)
        newHead = self.get(self.size - sizeDeBottomUp + 1)
        self.tail.nexts = self.head
        self.head = newHead
        self.tail = newTail
        newTail.nexts = None

    def riffle(self,factor):
        if factor <= 0 or factor >= 1:
            raise IOError('factor must in range 0 - 1')
        cutIndex = int(self.size * factor)

        self.tail = self.get(cutIndex)
        # self.tail.nexts = None
        for i in range(0,self.size - cutIndex):
            insertNode = node(self.get( i + cutIndex ).data)
            self.remove(i+cutIndex)
            self.insert(insertNode,i*2)
    
    def deRiffle(self,factor):
        if factor <= 0 or factor >= 1:
            raise IOError('factor must in range 0 - 1')
        
        

            

    
poke = Poke(1,10)
poke.riffle(0.6)
print(poke)
#poke.bottomUp(0.3)
# poke.riffle(0.6)
# print(poke)