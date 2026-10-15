class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BinaryTree:
    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.lchild is None:
                cur.lchild = node
                return
            else:
                queue.append(cur.lchild)
            if cur.rchild is None:
                cur.rchild = node
                return
            else:
                queue.append(cur.rchild)

    def travel(self):
        """按广度遍历整个内容"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)


if __name__ == '__main__':
    bt = BinaryTree(Node("桑多涅"))
    bt.add("哥伦比亚")
    bt.add("爱可菲")
    bt.add("菲谢尔")
    bt.add("奥黛塔")
    bt.travel()


