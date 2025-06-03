import unittest
class BSTree:

    class node:
         def __init__(self,val,left = None,right = None):
             self.val = val
             self.left = left
             self.right = right

    def __init__(self,root = None):
        self.root = root
        self.size = 0

    def add(self,val):
        if not self.root:
            self.root = self.node(val)
        else:
            self.insert(val,self.root)
        self.size += 1

    def insert(self,val,node):
        if not node:
            return self.node(val)
        if val > node.val:
            node.right = self.insert(val,node.right)
        else:
            node.left = self.insert(val,node.left)
        return node

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.val, end=' ')
            self.inorder(node.right)

    def preorder(self,node):
        if node:
            print(node.val, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)


    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=' ')



def test_bstree():
    print(" 创建 BST...")
    tree = BSTree()
    for val in [10, 5, 15, 3, 7, 12, 18]:
        tree.add(val)


    print("\n测试 1：中序遍历（应为排序结果）")
    print("预期输出：3 5 7 10 12 15 18")
    print("实际输出：", end="")
    tree.inorder(tree.root)
    print()

    print("\n 测试 2：树的大小")
    print("预期大小：7")
    print("实际大小：", tree.size)

    print("\n 测试 3：插入重复值 10 后，再次中序遍历")
    tree.add(10)  # 插入重复值
    print("预期输出包含两个 10，如：3 5 7 10 10 12 15 18")
    print("实际输出：", end="")
    tree.inorder(tree.root)
    print("\n实际大小（应该为 8）：", tree.size)

    print("\n 测试 4：单个值插入")
    tree2 = BSTree()
    tree2.add(99)
    print("树根值：", tree2.root.val)
    print("树大小：", tree2.size)

    print("\n 测试 5：先序遍历")
    print("预期输出（先访问根，再左，再右）：10 5 3 7 15 12 18 ...")
    print("实际输出：", end="")
    tree.preorder(tree.root)
    print()

    print("\n 测试 6：后序遍历")
    print("预期输出（左→右→根）：3 7 5 12 18 15 10 ...")
    print("实际输出：", end="")
    tree.postorder(tree.root)
    print()


if __name__ == "__main__":
    test_bstree()

