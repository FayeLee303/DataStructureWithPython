"""
循环队列包括两个指针，front指向队头，rear指向队尾
判断队列为空：front==rear
队列满：(rear+1)%maxsize == front
队列长度：(rear-front+maxsize)%maxsize
"""

class SqQueue(object):
    def __init__(self,maxsize):
        self.queue = [None]*maxsize
        self.maxsize = maxsize
        self.front = 0
        self.rear = 0

    # 长度
    def length(self):
        return (self.rear - self.front + self.maxsize)%self.maxsize

    # 队尾入队
    def in_queue(self,item):
        if (self.rear+1)%self.maxsize == self.front:
            print("队列已满！")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear+1)%self.maxsize

    # 队头出队
    def out_queue(self):
        if self.rear == self.front:
            print("队列为空！")
        else:
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front+1)%self.maxsize
            return item

    def travel(self):
        for i in range(self.maxsize):
            print(self.queue[i],end=",")
        print(' ')


if __name__ == "__main__":
    q = SqQueue(15)
    for i in range(10):
        q.in_queue(i)
    q.travel()
    for i in range(5):
        q.out_queue()
    q.travel()
    for i in range(8):
        q.in_queue(i)
    q.travel()
