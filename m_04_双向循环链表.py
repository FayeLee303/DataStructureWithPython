class CircularDoubleNode(object):
    def __init__(self,data):
        self.data = data
        self.next = None
        self.pre = None

class CircularDoubleLinkList(object):
    def __init__(self,node=None):
        if node is not None:
            # 后指针和前指针都指向头
            node.next = node
            node.pre = node
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        count = 0
        cur = self.__head
        if self.is_empty():
            return 0
        # 循环链表，当指针的next是头结点停止
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        # 不要忘了循环外面的尾结点！！
        count += 1
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
        # 头插法尾结点不变！！！

        newNode = CircularDoubleNode(data)
        # 空表时插入结点为头结点，指针指向自己
        if self.is_empty():
            self.__head = newNode
            self.__head.next = self.__head
            self.__head.pre = self.__head
        else:
            # 新结点插入到原来头结点之前
            newNode.next = self.__head
            newNode.pre = self.__head.pre
            self.__head.pre.next = newNode
            # 尾结点的next指向新的头结点！
            self.__head.pre = newNode

            self.__head = newNode

    # 尾插法
    def add_after_tail(self,data):
        # 尾插法头结点不变！！

        # 链表为空相当于头插
        if self.is_empty():
            self.add_before_head(data)
        else:
            newNode = CircularDoubleNode(data)
            # 新结点的前指向原来的尾结点
            newNode.pre = self.__head.pre
            # 新结点的后指向头结点
            newNode.next = self.__head
            # 原来尾结点的后指向新结点
            self.__head.pre.next = newNode
            # 头结点的前指向新结点
            self.__head.pre = newNode

    # 在指定位置插入
    def insert(self,index,data):
        # 小于0的都插在头结点之前
        if index < 0:
            self.add_before_head(data)
        elif index > self.length() - 1:
            # 超出边界的都插在尾结点之后
            self.add_after_tail(data)
        else:
            newNode = CircularDoubleNode(data)
            cur = self.__head
            pos = 0
            # 找到要插入位置的前一个结点
            while pos < index - 1:
                pos += 1
                cur = cur.next
            # 插入
            cur.next.pre = newNode
            newNode.next = cur.next
            cur.next = newNode
            newNode.pre = cur

    def remove(self,data):
        if self.is_empty() or (self.length()==1 and self.__head.data != data):
            return False
        elif self.length() == 1 and self.__head.data == data:
            # 表里只有一个元素就是所删元素
            # 让表为空
            self.__head = None
        else:
            cur = self.__head
            while cur.next != self.__head:
                if cur.data == data:
                    # 头结点，尾结点，中间结点都是一样的
                    cur.pre.next = cur.next
                    cur.next.pre = cur.pre
                    return
                else:
                    # 没有找到数据
                    cur = cur.next
            # 别忘了循环外的尾结点！！
            if cur.data == data:
                cur.pre.next = cur.next
                cur.next.pre = cur.pre
            else:
                # 没有找到数据
                return False

    def search(self,data):
        if self.is_empty():
            return False
        else:
            # 定义两个指针，从头尾开始遍历，两指针重叠或者相遇时结束(长度可偶可奇)
            cur_1 = self.__head
            cur_2 = self.__head.pre
            length = self.length()
            index_1 = 0     # 正数第一个就返回
            index_2 = length    # 倒数如果有相同的，返回下标最小的
            index_2_list = []
            # 两指针相遇时结束或者重叠时结束
            while cur_1.next != cur_2 or cur_1 != cur_2:
                if cur_1.data == data:
                    return index_1
                if cur_2.data == data:
                    # 还没到结束条件，万一有多个相同值
                    # 要返回下标小的那个
                    index_2_list.append(index_2)
                cur_1 = cur_1.next
                index_1 += 1
                cur_2 = cur_2.pre
                index_2 -=1
            # 执行到这一步说明没有return index_1
            # index2list里有东西，说明找到了
            # 返回list里最后一个，就是下标最小的
            if len(index_2_list) > 0:
                return index_2_list[len(index_2_list) - 1]
            # 没有找到数据
            else:
                return False
            # if length%2 == 0:
            #     # 两指针相遇时结束
            #     while cur_1.next != cur_2:
            #         if cur_1.data == data:
            #             return index_1
            #         if cur_2.data == data:
            #             # 还没到结束条件，万一有多个相同值
            #             # 要返回下标小的那个
            #             index_2_list.append(index_2)
            #         cur_1 = cur_1.next
            #         index_1 += 1
            #         cur_2 = cur_2.pre
            #         index_2 = length - 1
            #     # 执行到这一步说明没有return index_1
            #     # index2list里有东西，说明找到了
            #     # 返回list里最后一个，就是下标最小的
            #     if len(index_2_list)>0:
            #         return index_2_list[len(index_2_list)-1]
            #     # 没有找到数据
            #     return False
            # elif length%2 != 0:
            #     # 两指针重叠时结束
            #     while cur_1 == cur_2:
            #         if cur_1.data == data:
            #             return index_1
            #         if cur_2.data == data:
            #             # 还没到结束条件，万一有多个相同值
            #             # 要返回下标小的那个
            #             index_2_list.append(index_2)
            #         cur_1 = cur_1.next
            #         index_1 += 1
            #         cur_2 = cur_2.pre
            #         index_2 = length - 1
            #     # 执行到这一步说明没有return index_1
            #     # index2list里有东西，说明找到了
            #     # 返回list里最后一个，就是下标最小的
            #     if len(index_2_list) > 0:
            #         return index_2_list[len(index_2_list) - 1]
            #     # 没有找到数据
            #     return False

    # 获得指定位置上数据
    def index(self,pos):
        if pos<0 or pos>self.length():
            print("索引超出边界！")
            return
        else:
            # 减治法
            # 定义两个指针，从头尾开始遍历，两指针重叠或者相遇时结束
            cur_1 = self.__head
            cur_2 = self.__head.pre
            length = self.length()
            index_1,index_2 = 0,length
            while cur_1.next != cur_2 or cur_1 != cur_2:
                if index_1 == pos:
                    return cur_1.data
                if index_2 == pos:
                    return cur_2.data
                cur_1 = cur_1.next
                index_1 += 1
                cur_2 = cur_2.pre
                index_2 -= 1
            # 没有找到数据
            return False

if __name__ == "__main__":
    list = CircularDoubleLinkList()
    list.add_before_head(1)
    list.add_before_head(2)
    list.add_before_head(3)
    list.add_after_tail(4)
    list.add_after_tail(5)
    print("是否为空：%s，长度：%d" % (list.is_empty(), list.length()))
    list.insert(2, 6)
    list.travel()

    print(list.search(3))
    print(list.search(6))
    list.remove(6)
    list.travel()

    print(list.index(4))








