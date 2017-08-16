class Stack:
    def __init__(self, lists = None):
        if lists == None:
            self.items = []
        else:
            self.items = lists 
        print(self.items)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def push(self,obj):
        self.items.append(obj)

    def print_stack(self):
        print(self.items)

p = Stack(['eiei','kiki'])
print(p.pop())
p.push('eiei')
p.print_stack()
