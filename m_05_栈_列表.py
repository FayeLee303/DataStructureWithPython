"""用列表实现"""
class Stack(object):
    # 限定Stack类的成员只有__items类成员
    __slots__ = ('__items')

    # 初始化栈为空列表
    def __init__(self):
        self.__items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.__items == []

    # 返回栈顶元素
    def peek(self):
        if self.is_empty():
            return None
        return self.__items[len(self.__items)-1]

    # 栈大小
    def size(self):
        return len(self.__items)

    # 入栈
    def push(self,item):
        self.__items.append(item)

    # 出栈
    def pop(self):
        # python的list自带pop
        return self.__items.pop()

    def clear(self):
        self.__items.clear()

if __name__ == "__main__":
    m_stack = Stack()
    m_stack.push('d')
    m_stack.push('s')
    m_stack.push(3)
    m_stack.push(2)
    print(m_stack.size())
    print(m_stack.peek())
    print(m_stack.pop())
    print(m_stack.size())
    print(m_stack.peek())
    print(m_stack.is_empty())
