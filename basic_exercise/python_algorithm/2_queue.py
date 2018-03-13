#20180313
class Queue:
    """模拟队列"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    #在队列尾部加入一个数据项，参数是数据项，无返回值。
    def enqueue(self, item):
        self.items.insert(0, item)

    #删除队列头部的数据项，不需要参数，返回值是被删除的数据，队列本身有变化。
    def dequeue(self):
        return self.items.pop()

    #返回队列数据项的数量。无参数，返回一个整数。
    def size(self):
        return len(self.items)


q = Queue()
print(q.isEmpty())

q.enqueue('dog')
q.enqueue(4)
print(q.items)

q = Queue()
print(q.isEmpty())

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.items)
q.dequeue()
print(q.items)