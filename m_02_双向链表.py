class DoubleNode(object):
    """双链表结点"""
    def __init__(self,data):
        self.data = data
        self.next = None
        self.pre = None

class DoubleLinkList(object):
    """双链表"""
    def __init__(self,node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        count = 0
        # 定义一个游标用于遍历整个链表，初始时指向表头指向的内容
        # 如果头结点为空，返回None
        cur = self.__head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print(" ")

    # 头插法
    def add_before_head(self,data):
        # 新结点的next指向原来的表头
        # 原来表头的pre指向新结点
        # 表头指向新结点
        newNode = DoubleNode(data)
        if self.__head is None:
            self.__head = newNode
        else:
            newNode.next = self.__head
            self.__head.pre = newNode
            self.__head = newNode

    # 尾插法
    def add_after_tail(self,data):
        newNode = DoubleNode(data)
        # 如果是空表，新结点成为表头
        if self.is_empty():
            self.__head = newNode
        else:
            # 找最后一个结点
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode
            newNode.pre = cur

    # 在指定位置插入
    def insert(self, index, data):
        if index < 0 or index > self.length():
            print("索引位置越界！")
        elif index == 0:
            self.add_before_head(data)
        elif index == self.length():
            self.add_after_tail(data)
        else:
            newNode = DoubleNode(data)
            cur = self.__head
            pos = 0
            # 找到要插入位置的前一个结点
            while pos < index - 1:
                pos += 1
                cur = cur.next
            # 插入
            newNode.next = cur.next
            cur.next.pre = newNode
            cur.next = newNode
            newNode.pre = cur

    # 删除
    def remove(self, data):
        cur = self.__head  # 定义游标(指向当前位置)
        while cur is not None:
            if cur.data == data:
                # 删除头结点
                if cur == self.__head:
                    cur.next.pre = self.__head
                    self.__head = cur.next
                else:
                    # 将上一个节点的next指向当前节点的next
                    # 也就是当前节点的下一个节点位置
                    cur.pre.next = cur.next
                    cur.next.pre = cur.pre
                break
            else:
                # 指针向后移动
                cur = cur.next
        # 没有找到数据
        return False

    # 搜索
    def search(self, data):
        index = 0
        cur = self.__head
        while cur is not None:
            if cur.data == data:
                # 返回下标
                return index
            index += 1
            cur = cur.next
        # 没有找到
        return -1

    # 获得指定位置上的数据
    def index(self, pos):
        if pos<0 or pos>self.length():
            print("索引超出边界！")
            return
        index = 0
        cur = self.__head
        while cur is not None:
            if index == pos:
                return cur.data
            else:
                cur = cur.next
                index += 1
        # 没有找到
        return None

if __name__ == "__main__":
    list = DoubleLinkList()
    list.add_before_head(1)
    list.add_before_head(2)
    list.add_before_head(3)
    list.add_after_tail(4)
    list.insert(2,"sss")
    print("是否为空：%s，长度：%d" % (list.is_empty(), list.length()))
    list.travel()
    list.insert(0, 'ooo')
    list.insert(-1, 'aaa')
    print(list.search("sss"))
    list.remove(3)
    list.travel()
    list.remove("ooo")
    list.travel()

    print(list.index(4))

    newNode = DoubleNode("hhhhh")
    list2 = DoubleLinkList(newNode)
    print("是否为空：%s，长度：%d" % (list2.is_empty(), list2.length()))
