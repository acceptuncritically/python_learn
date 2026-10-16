# 包括先序 中序 后序


class Node:
    def __init__(self, item):
        self.item = item
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
    def preorder_travel(self,root):
        # 递归时"根" 会一层层往下变
        if root is not None:
            print(root.item,end=" ")
            #遍历左子树
            self.preorder_travel(root.lchild)
            self.preorder_travel(root.rchild)
    def inorder_travel(self,root):
        if root is not None:
            self.inorder_travel(root.lchild)
            print(root.item,end=" ")
            self.inorder_travel(root.rchild)
    def postorder_travel(self,root):
        if root is not None:
            self.postorder_travel(root.lchild)
            self.postorder_travel(root.rchild)
            print(root.item,end=" ")
if __name__ == '__main__':
    bt = BinaryTree()
    bt.add("桑多涅")
    bt.add("哥伦比亚")
    bt.add("爱可菲")
    bt.add("菲谢尔")
    bt.add("奥黛塔")
    bt.preorder_travel(bt.root)
    #第一次调用时，还没有"当前节点"的概念，需要人为指定从哪开始 → 那就从整棵树的根 bt.root 开始
    print()
    bt.inorder_travel(bt.root)
    print()
    bt.postorder_travel(bt.root)
