from collections import deque
class Stack():

    def __init__(self):
        self.container=deque()

    def push(self,value):
        self.container.append(value)

    def pop(self):
        self.container.pop()

    def empty(self):
        if len(self.container)==0:
            return True
        else:
            return False

    def size(self):
        return len(self.container)

    def printS(self):
        print('why',self.container)
        return self.container

obj=Stack()
obj.push(1)
obj.push(3)
obj.push(5)
print(obj.printS())

