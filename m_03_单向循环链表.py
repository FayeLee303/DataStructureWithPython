class CircularSingleNode(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularSingleLinkList(object):
    def __init__(self,node=None):
        if node is not None:
            # 尾指针指向头
            node.next = node
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        count = 0
        cur = self.__head
        if self.is_empty():
            return 0
        # 循环链表，当指针的next是头结点停止
        while cur.next != self.__head:
            count +=1
            cur = cur.next
        # 不要忘了循环外面的尾结点！！
        count +=1
        return count

    # 遍历
    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.data, end=" ")
            cur = cur.next
        # 退出循环时，cur正是尾节点
        print(cur.data)

    # 头插法
    def add_before_head(self, data):
        newNode = CircularSingleNode(data)
        # 空表时插入结点为头结点，指针指向自己
        if self.is_empty():
            self.__head = newNode
            self.__head.next = self.__head
        else:
            cur = self.__head
            # 遍历链表找到尾结点！
            while cur.next != self.__head:
                cur = cur.next
            # 新结点插入到原来头结点之前
            newNode.next = self.__head
            self.__head = newNode
            # 尾结点的next指向新的头结点！
            cur.next = self.__head

    # 尾插法
    def add_after_tail(self, data):
        newNode = CircularSingleNode(data)
        # 如果是空表，新结点成为表头，指针指向自己
        if self.is_empty():
            self.__head = newNode
            self.__head.next = self.__head
        else:
            # 找最后一个结点
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 新结点的next指向原来尾结点的next也就是头结点
            newNode.next = cur.next
            cur.next = newNode

    # 在指定位置插入
    def insert(self, index, data):
        # 小于0的都插在头结点之前
        if index < 0:
            self.add_before_head(data)
        elif index > self.length() -1:
            # 超出边界的都插在尾结点之后
            self.add_after_tail(data)
        else:
            newNode = CircularSingleNode(data)
            cur = self.__head
            pos = 0
            # 找到要插入位置的前一个结点
            while pos < index - 1:
                pos += 1
                cur = cur.next
            # 插入
            newNode.next = cur.next
            cur.next = newNode

    # 删除
    def remove(self,data):
        if self.is_empty():
            return False
        elif self.length() == 1 and self.__head.data == data:
            # 表里只有一个元素就是所删元素
            # 让表为空
            self.__head = None
        else:
            cur = self.__head
            # 用来记录前一个结点
            pre = None
            # 找到尾结点
            temp = self.__head
            while temp.next != self.__head:
                temp = temp.next

            while cur.next != self.__head:
                if cur.data == data:
                    if cur == self.__head:
                        # 如果所删结点是头结点
                        self.__head = cur.next
                        temp.next = self.__head
                    else:
                        # 删除结点在中间或者是尾结点一样的
                        pre.next = cur.next
                else:
                    # 没有找到数据
                    pre = cur
                    cur = cur.next
            # 别忘了循环外的尾结点！！！
            if cur.data == data:
                pre.next = cur.next
            else:
                # 遍历完了没有找到数据返回False
                return False

    def search(self,data):
        if self.is_empty():
            return False
        cur = self.__head
        index = 0
        while cur.next != self.__head:
            if cur.data == data:
                # 返回下标
                return index
            index += 1
            cur = cur.next
        # 别忘了循环外的尾结点！！！
        if cur.data == data:
            index += 1
            return index
        # 没有找到数据
        return False

    # 获得指定位置上的数据
    def index(self,pos):
        if pos<0 or pos>self.length():
            print("索引超出边界！")
            return
        index = 0
        cur = self.__head
        while cur.next != self.__head:
            if index == pos:
                return cur.data
            else:
                cur = cur.next
                index += 1
        # 别忘了循环外的尾结点！！！
        if pos == self.length():
            return cur.data
        # 没有找到
        return None


if __name__ == "__main__":
    list = CircularSingleLinkList()
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

    print(list.search("3"))

    list.remove(3)
    list.travel()
    list.remove("ooo")
    list.travel()

    print(list.index(4))

    newNode = CircularSingleNode("hhhhh")
    list2 = CircularSingleLinkList(newNode)
    print("是否为空：%s，长度：%d" % (list2.is_empty(), list2.length()))
