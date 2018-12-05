"""
左子树不为空时，左子树上所有结点都小于根结点
右子树不为空时，右子树上所有结点都小于根结点
左右子树也分别是二叉排序树
查找：小了往左子树去找，大了往右子树去找
插入：小了去左，大了去右
删除：
    如果删除的结点是叶子，直接删除
    如果要删除结点只有左子树或者只有右子树，则删除结点后将子结点连到父结点上
    如果要删除结点同时有左右子树，则可以将二叉排序树中序遍历
取将要删除结点的前驱或者后继代替这个被删除的结点的位置
    如果要删除结点同时有左右子树，取其右子树的最小结点代替该结点，调整完之后
该树应该呈现是度为1的结点的子结点在左

二叉排序树的中序遍历是把这些数从小到大排列！！
"""

class BSTNode(object):
    def __init__(self,data):
        self.data = data
        self.rchild = None
        self.lchild = None

class BinarySortTree(object):
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    # 查找
    def search(self,key):
        node = self.root
        # 比当前结点小，去当前结点的左子树找
        # 比当前结点大，去当前结点的右子树找
        while node:
            temp = node.data
            if key < temp:
                node = node.lchild
            elif key > temp:
                node = node.rchild
            else:
                return temp
        # 没找到
        return None

    # 递归版本搜索
    def search_digui(self,root,key):
        if root is None:
            return None
        else:
            if key > root.data:
                return self.search_digui(root.rchild,key)
            elif key < root.data:
                return self.search_digui(root.lchild, key)
            else:
                return root

    # 插入
    def insert(self,key):
        node = BSTNode(key)
        # 如果是空，新结点成为根结点
        if self.is_empty():
            self.root = node
        # 如果已经有这个值就不插入直接返回
        elif self.search(key) is not None:
            return
        else:
            temp = self.root
            # 小了去左，大了去右
            while True:
                if node.data < temp.data:
                    if temp.lchild is None:
                        temp.lchild = node
                        return
                    else:
                        temp = temp.lchild
                elif node.data > temp.data:
                    if temp.rchild is None:
                        temp.rchild = node
                        return
                    else:
                        temp = temp.rchild

    # 删除
    def delet(self,key):
        # 维持p是q的父结点，用于后面的链接操作
        p,q = None,self.root
        if self.is_empty():
            print("是空树！")
            return
        else:
            while q and q.data!=key:
                # 维持p是q的父结点
                p = q
                if key < q.data:
                    q = q.lchild
                elif key > q.data:
                    q = q.rchild
                # 遍历完没有key时return
                if not q:
                    return
            # 已经找到了要删除的结点，用q指向，p是q的父结点，如果q是根结点，p是None
            # 如果q是根结点，让树为空
            if q is self.root:
                self.root = None
            # 如果q是叶子结点，直接删除
            elif q.rchild is None and q.lchild is None:
                if q is p.lchild:
                    p.lchild = None
                else:
                    p.rchild = None
            # 如果q只有左子树或者只有右子树，则删除结点后将子结点连到父结点p上
            elif q.lchild is not None and q.rchild is None:
                if q is p.lchild:
                    p.lchild = q.lchild
                else:
                    p.rchild = q.lchild
            elif q.lchild is None and q.rchild is not None:
                if q is p.lchild:
                    p.lchild = q.rchild
                else:
                    p.rchild = q.rchild
            # 如果q左右子树都有，取其右子树的最小结点代替该结点
            else:
                # temp是q右子树的最小结点
                # temp_root是temp的父结点
                temp = q.rchild
                temp_root = None
                while temp.lchild:
                    temp_root = temp
                    temp = temp.lchild
                # 这是把temp摘出来
                temp_root.lchild = None
                # 用temp取代q
                temp.rchild = q.rchild
                if q is p.lchild:
                    p.lchild = temp
                elif q is p.rchild:
                    p.rchild = temp

    """用递归实现遍历"""
    # 先序遍历
    def pre_order(self,root):
        if root is None:
            return None
        else:
            print(root.data)
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # 中序
    def in_order(self,root):
        if root is None:
            return None
        else:
            self.in_order(root.lchild)
            print(root.data)
            self.in_order(root.rchild)

    # 后序
    def post_order(self, root):
        if root is None:
            return None
        else:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data)


if __name__ == "__main__":
    t = BinarySortTree()
    arr = [17,12,25,10,15,13,16,21,19,26]
    for i in arr:
        t.insert(i)
    print(t.is_empty())
    print(t.search(13))
    print(t.search_digui(t.root,13))

    print("先序遍历%s"%t.pre_order(t.root))
    print("中序遍历%s" % t.in_order(t.root))
    print("后序遍历%s" % t.post_order(t.root))

    t.delet(12)

    print("先序遍历%s" % t.pre_order(t.root))
    print("中序遍历%s" % t.in_order(t.root))
    print("后序遍历%s" % t.post_order(t.root))






