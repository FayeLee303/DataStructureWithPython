class SingleNode(object):
    """单链表结点"""
    def __init__(self,data):
        self.data = data    # 数据
        self.next = None    # 指针

class SingleLinkList(object):
    """单链表"""
    def __init__(self,node = None):
        # 定义表头，方便操作使用，由于是类内部使用，所以定义为私有变量
        self.__head = node

    # 判断是否为空，表头为空
    def is_empty(self):
        return self.__head == None

    # 求长度
    def length(self):
        count = 0
        # 定义一个游标用于遍历整个链表，初始时指向表头指向的内容
        # 如果头结点为空，返回None
        cur = self.__head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    # 遍历
    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.data,end=" ")
            cur = cur.next
        print(" ")

    # 头插法
    def add_before_head(self,data):
        # 新结点的next指向原来的表头
        # 表头指向新结点
        newNode = SingleNode(data)
        newNode.next = self.__head
        self.__head = newNode

    # 尾插法
    def add_after_tail(self,data):
        newNode = SingleNode(data)
        # 如果是空表，新结点成为表头
        if self.is_empty():
            self.__head = newNode
        else:
            # 找最后一个结点
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode

    # 在指定位置插入
    def insert(self,index,data):
        if index<0 or index>self.length():
            print("索引位置越界！")
        elif index == 0:
            self.add_before_head(data)
        elif index == self.length():
            self.add_after_tail(data)
        else:
            newNode = SingleNode(data)
            cur = self.__head
            pos = 0
            # 找到要插入位置的前一个结点
            while pos < index -1:
                pos += 1
                cur = cur.next
            # 插入
            newNode.next = cur.next
            cur.next = newNode

    # 删除
    def remove(self,data):
        cur = self.__head    # 定义游标(指向当前位置)
        pre = None          # 定义游标(指向上一个节点位置）
        while cur is not None:
            if cur.data == data:
                # 删除头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    # 将上一个节点的next指向当前节点的next
                    # 也就是当前节点的下一个节点位置
                    pre.next = cur.next
                break
            else:
                # 指针向后移动
                pre = cur
                cur = cur.next
        # 没有找到数据
        return False

    # 搜索
    def search(self,data):
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
    def index(self,pos):
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
    list = SingleLinkList()
    print("是否为空：%s，长度：%d"%(list.is_empty(),list.length()))

    list.add_before_head(1)
    list.add_after_tail(2)
    list.add_after_tail(3)
    list.insert(2,4)
    print("是否为空：%s，长度：%d" % (list.is_empty(), list.length()))
    list.travel()

    list.insert(0, 'ooo')
    list.insert(-1, 'aaa')
    list.insert(4, 'bbbb')
    list.insert(7, 'cccc')
    print("是否为空：%s，长度：%d" % (list.is_empty(), list.length()))
    list.travel()

    print(list.search("aaa"))

    list.remove(3)
    list.travel()
    list.remove("ooo")
    list.travel()

    print(list.index(4))

    newNode = SingleNode("hhhhh")
    list2 = SingleLinkList(newNode)
    print("是否为空：%s，长度：%d" % (list2.is_empty(), list2.length()))

