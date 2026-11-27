class Queue:
    def __init__(self):
        self.__list = []
    def enqueue(self, value):
        self.__list.append(value)
    def dequeue(self):
        return self.__list.pop(0)
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
