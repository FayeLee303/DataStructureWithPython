"""用列表实现"""
class Queue(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def length(self):
        return len(self.queue)

    # 一次入队一个
    def in_queue_one(self,item):
        self.queue.append(item)


    # 一次入队多个
    def in_queue_many(self,*args):
        self.queue.extend(args)

    # 出队
    def out_queue(self):
        if self.is_empty():
            return None
        else:
            # 先进先出，出队首元素
            self.queue.pop(0)

    def travel(self):
        for i in self.queue:
            print(i)

    # 队头
    def head(self):
        if self.is_empty():
            return None
        else:
            print(self.queue[0])

    # 队尾
    def tail(self):
        if self.is_empty():
            return None
        else:
            print(self.queue[-1])

if __name__ == "__main__":
    q1 = Queue()
    q1.in_queue_one(0)
    q1.travel()
    q1.in_queue_many(9,3,2)
    q1.travel()
    q1.out_queue()
    q1.travel()
    q1.head()
    q1.tail()
    print(q1.length())
    print(q1.is_empty())

