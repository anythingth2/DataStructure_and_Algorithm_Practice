class CarStack:
    def __init__(self):
        self.MAX_SIZE = 4
        self.stack = []
    
    def isFull(self):
        return len(self.stack) >= self.MAX_SIZE
    def depart(self,car):
        if car in self.stack:
            self.stack.remove(car)
        else:
            if len(self.stack) == 0:
                print('cannot depart : soi empty')
            else:
                print('cannot depart : not found')

    def arrive(self,car):
        if int(car) in range(1,self.MAX_SIZE+1) and not self.isFull():
            self.stack.append(car,int(car))
            print('space left',self.MAX_SIZE - len(self.stack))
        else:
            if self.isFull():
                print('cannot arrive : soi full')
            else:
                print('cannot arrive : No car',car)

