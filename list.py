class node:
    def __init__(self,data,nexts = None):
        self.data = data
        self.nexts = nexts 
    def __str__(self):
        return str(self.data)

class List:

    def __init__(self,data = None):
        self.head = self.tail = node(data)
        self.size = 0 if data == None else 1
    def __str__(self):
        for i in range(self.size):
            print(self.get(i),end=' ')

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
    
    def appendRecursion(self,dataList):
        
        if len(dataList) == 1:
            self.append(dataList.pop(0))
        else:
            self.append(dataList.pop(0))
            self.appendRecursion(dataList)

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

class CircularList:

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
        if index >= self.size:
            index = index % self.size
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


