"""
二叉树第i层上结点数目最多为2的i-1次方,i>=1
深度为k的二叉树最多有2的k次方-1个结点，k>=1
包含n个结点的二叉树的高度至少为logn+1，底为2
在任意一棵二叉树中，如果终端结点的个数为n0,度为2的结点是n2,则n0=n2+1
"""

"""结点"""
class Node(object):
    def __init__(self,item):
        self.item = item
        self.rchild = None
        self.lchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    # 求树的深度，分治法
    def max_depth(self,root):
        if root is None:
            return 0
        else:
            left_height = self.max_depth(root.lchild)
            right_height = self.max_depth(root.rchild)
            # +1是算上根结点
            return max(left_height,right_height)+1

    # 使用栈和深度优先搜索DFS
    def max_depth_2(self,root):
        stack = []
        if root is not None:
            stack.append((1,root))
        depth = 0
        while stack != []:
            current_depth,root = stack.pop()
            if root is not None:
                depth = max(depth,current_depth)
                stack.append((current_depth+1,root.lchild))
                stack.append((current_depth+1,root.rchild))
        return depth


    # 添加新叶子结点
    def add(self,item):
        node = Node(item)
        # 如果树为空，新结点成为根结点
        if self.is_empty():
            self.root = node
        else:
            # 使用队列实现按层遍历，然后添加结点
            queue = [self.root]
            while True:
                # 拿出队头
                pop_node = queue.pop(0)
                # 找空位添加新结点
                if pop_node.lchild is None:
                    pop_node.lchild = node
                    return
                elif pop_node.rchild is None:
                    pop_node.rchild = node
                    return
                # 没有空位，继续找空位
                else:
                    queue.append(pop_node.lchild)
                    queue.append(pop_node.rchild)

    # 利用队列实现树的层次遍历
    def traverse(self):
        if self.is_empty():
            return None
        queue = [self.root]
        res = [self.root.item]
        while queue!=[]:
            pop_node = queue.pop(0)
            if pop_node.lchild is not None:
                queue.append(pop_node.lchild)
                res.append(pop_node.lchild.item)
            if pop_node.rchild is not None:
                queue.append(pop_node.rchild)
                res.append(pop_node.rchild.item)
        return res

    # # 利用队列实现树的层次遍历
    # def level_queue(self):
    #     if self.is_empty():
    #         return None
    #     my_queue = []
    #     result = []
    #     while my_queue:
    #         # 队头出队
    #         node = my_queue.pop(0)
    #         # print(node.item)
    #         result.append(node.item)
    #         if node.lchild:
    #             my_queue.append(node.lchild)
    #         if node.rchild:
    #             my_queue.append(node.rchild)
    #     return result


    """使用递归实现树的遍历"""
    # 先序遍历
    def pre_order(self,root):
        res = []
        if root is None:
            return res
        else:
            res = [root.item]
            left = self.pre_order(root.lchild)
            right = self.pre_order(root.rchild)
            return res + left + right

    # 中序遍历
    def in_order(self,root):
        res = []
        if root is None:
            return res
        else:
            res = [root.item]
            left = self.in_order(root.lchild)
            right = self.in_order(root.rchild)
            return left + res + right

    # 后序遍历
    def post_order(self,root):
        res = []
        if root is None:
            return res
        else:
            res = [root.item]
            left = self.post_order(root.lchild)
            right = self.post_order(root.rchild)
            return left + right + res
    """使用栈实现树的遍历"""
    # 先序
    def pre_stack(self):
        if self.is_empty():
            return None
        my_stack = []
        node = self.root
        result = []
        while node or my_stack:
            # 从根结点开始，一直找左子树
            while node:
                # 访问根
                # print(node.item)
                result.append(node.item)
                my_stack.append(node)
                node = node.lchild
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = my_stack.pop()
            # 开始查看它的右子树
            node = node.rchild
        return result

    # 中序
    def in_stack(self):
        if self.is_empty():
            return None
        my_stack = []
        node = self.root
        result = []
        while node or my_stack:
            # 从根结点开始，一直找他的左子树
            while node:
                my_stack.append(node)
                node = node.lchild
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = my_stack.pop()
            # 访问根结点
            # print(node.item)
            result.append(node.item)
            # 开始查看它的右子树
            node = node.rchild
        return result

    # 后序
    def post_stack(self):
        if self.is_empty():
            return None
        my_stack_1 = []
        my_stack_2 = []
        node = self.root
        my_stack_1.append(node)
        result = []
        # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
        while my_stack_1:
            node = my_stack_1.pop()
            if node.lchild:
                my_stack_1.append(node.lchild)
            if node.rchild:
                my_stack_1.append(node.rchild)
            my_stack_2.append(node)
        # 将myStack2中的元素出栈，即为后序遍历次序
        while my_stack_2:
            # 访问根
            # print(my_stack_2.pop().item)
            result.append(my_stack_2.pop().item)
        return result


if __name__ =="__main__":
    t = Tree()
    for i in range(10):
        t.add(i)

    print("层序遍历%s"%t.traverse())
    # print("队列层序遍历%s"%t.level_queue())
    print("=====使用递归=====")
    print("先序遍历%s"%t.pre_order(t.root))
    print("中序遍历%s"%t.in_order(t.root))
    print("后序遍历%s"%t.post_order(t.root))
    print("=====使用栈=====")
    print("先序遍历%s" % t.pre_stack())
    print("中序遍历%s" % t.in_stack())
    print("后序遍历%s" % t.post_stack())



