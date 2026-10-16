class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
class BinaryTree:
    def __init__(self, node=None):
        self.root = node
    def add(self, item):
        new_node = Node(item)
        if self.root is None:
            self.root = new_node
            return
        queue = [self.root]
        while True:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = new_node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = new_node
                return
            else:
                queue.append(cur_node.rchild)
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
    bt = BinaryTree()
    bt.add("桑多涅")
    bt.add("哥伦比亚")
    bt.add("爱可菲")
    bt.add("菲谢尔")
    bt.add("奥黛塔")
    bt.travel()


