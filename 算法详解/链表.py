"""
单链表是链表的一种形式
链表是由节点组成的一条式子 每个节点只能有一个前驱和一个后继结点
节点有链接域和地址域
用于优化顺序表的弊端
自定义代码模拟链表：
    自定义SingleNode类 ：表示节点
    属性：
        item 数值域
        next 地址域
    自定义SingleLinkedList类：表示：链表
    属性：
        head 表示头节点 指向第一个节点
    行为：
        is_empty(self)          链表是否为空
        length(self)            链表长度
        travel(self. )          遍历整个链表
        add(self, item)         链表头部添加元素
        append(self, item)      链表尾部添加元素
        insert(self, pos, item) 指定位置添加元素
        remove(self, item)      删除节点
        search(self, item)      查找节点是否存在
    测试：
"""
class SingleNode:
    #初始化属性
    def __init__(self,item):
        self.item = item
        self.next = None
class SingleLinkedList:
    #初始化属性
    def __init__(self,node=None):
        self.head =node #链表的头节点指向第一个节点
    def is_empty(self):

        # if self.head is None:
        #     return True
        # return False

        return self.head is None
    def length(self):
        #创建游标表示当前节点
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count
    def travel(self):
        cur = self.head
        while cur:
            print(cur.item)
            cur = cur.next
    def add(self,item):
        new_node = SingleNode(item)
        new_node.next = self.head
        self.head = new_node
    def append(self,item):#在末尾添加节点
        new_node = SingleNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            #链表不为空需要找到尾节点
            #创建游标（表示当前节点） 默认从头结点开始
            cur=self.head
            # 开始遍历只要当前节点不为空 就一直循环
            while cur.next:
                cur = cur.next
            # 最后一个节点
            cur.next = new_node
    def insert(self,pos,item): #在指定位置前增加节点
        if pos<=0:
            #往前面加内容
            self.add(item)
        elif pos>=self.length():
            self.append(item)
        else:
            #从头结点开始创建游标
            cur=self.head
            count=0
            while count<pos:
                cur=cur.next
                count+=1
            new_node = SingleNode(item)
            new_node.next = cur.next
            cur.next = new_node
    def remove(self,item): #根据元素来删除节点
        cur=self.head
        # 定义要删除的前驱节点
        prev=None
        while cur:
            if cur.item == item:
                if cur==self.head:
                    self.head = cur.next
                else:
                    #说明要删除的节点不是头节点 直接设置前驱节点指向当前节点的下一节点
                    prev.next = cur.next
                    cur.next=None
                return
            else:
                #当前节点不是要删除的节点
                prev=cur
                cur=cur.next
    def search(self,item): #检查当前节点是否存在
        cur=self.head
        while cur:
            if cur.item == item:
                return True
            cur=cur.next
        return False
if __name__ == '__main__':
    node1 = SingleNode("桑多涅")
    print(f"元素域：{node1.item}")
    print(f"链接域：{node1.next}")
    print(f"{type(node1)}")
    my_list = SingleLinkedList(node1)
    print(f"头节点：{my_list.head}")
    print(f"头节点的元素域：{my_list.head.item}")
    print(f"头节点的地址域：{my_list.head.next}")
    print("---------------------------------------")
    print(my_list.is_empty())
    print(my_list.length())
    print("-------------------------------------------")
    my_list.add("哥伦比亚")
    my_list.append("仆人")
    my_list.insert(1,"散兵")
    my_list.remove("散兵")
    # my_list.remove("桑多涅")
    print(my_list.search("哥伦比亚"))
    my_list.travel()

