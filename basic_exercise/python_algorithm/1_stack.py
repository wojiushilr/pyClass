class Stack:
    #模拟堆栈
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)==0

    def push(self,item):
        #把一个元素添加到栈的最顶层
        self.items.append(item)

    def pop(self):
        #删除栈最顶层的元素，并返回这个元素
        return self.items.pop()

    def peek(self):
        #返回最顶层的元素，并不删除它
        if not self.isEmpty():
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()
print("s.isEmpty():",s.isEmpty())
s.push(4)
s.push("dog")
print("s.items:",s.items)
print("s.peek():",s.peek())

s.push(True)
print("s.items",s.items)

s.push(8.4)
print("s.items",s.items)

print("s.pop()",s.pop())
print("s.items",s.items)

print("s.pop()",s.pop())