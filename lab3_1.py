class Queue:
    def  __init__(self,size=None,queue=None):
        if queue == None:
            self.queue = []
        else:
            self.queue = queue
        self.size = size

    def __str__(self):
        return str(self.queue)
    def enQueue(self,i):
        if not self.isFull():
            self.queue.append(i)

    def deQueue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue)==0

    def isFull(self):
        return len(self.queue) == self.size

    def size(self):
        return len(self.queue)