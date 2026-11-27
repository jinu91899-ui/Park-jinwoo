class Stack:
    def __init__(self):
        self.__list = []
    def push(self,value):
        self.__list.append(value)
    def pop(self):
        return self.__list.pop()
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.pop())
print(stack.pop())