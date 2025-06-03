import unittest


class doulelink:

    class _node:
        def __init__(self,val,predecessor,successor):
            self.value = val
            self.next = successor
            self.pre = predecessor
    def __init__(self):
        self.ptr_head = self._node(None,None,None)
        self.ptr_tail = self._node(None,None,None)
        self.ptr_tail.pre = self.ptr_head
        self.ptr_head.next = self.ptr_tail
        self.size = 0

    def insert_btw(self,predecessor,successor,val):
        newnode = self._node(val,predecessor,successor)
        successor.pre = newnode
        predecessor.next = newnode
        self.size += 1
        return newnode

    def delete(self,tar):
        pre = tar.pre
        next = tar.next
        pre.next =next
        next.pre = pre
        self.size -= 1

    def is_empty(self):
        return self.size == 0

    def len(self):
        return self.size

    def traverse_back(self):
        temp = self.ptr_tail.pre
        while temp.pre:
            print(temp.value)
            temp = temp.pre

    def traverse_forward(self):
        temp = self.ptr_head.next
        while temp.next:
            print(temp.value)
            temp = temp.next


class TestDoubleLink(unittest.TestCase):
    def setUp(self):
        # 每个 test 之前都会重新创建一个空链表
        self.dl = doulelink()

    def test_insert_and_len(self):
        # 插入三个节点后长度应为 3
        n1 = self.dl.insert_btw(self.dl.ptr_head, self.dl.ptr_tail, 10)
        self.dl.insert_btw(n1,       self.dl.ptr_tail, 20)
        self.dl.insert_btw(n1,       self.dl.ptr_tail, 30)
        self.assertEqual(self.dl.len(), 3)

    def test_delete(self):
        # 插入后再删除，长度减少
        n1 = self.dl.insert_btw(self.dl.ptr_head, self.dl.ptr_tail, 100)
        self.dl.delete(n1)
        self.assertEqual(self.dl.len(), 0)

    def test_traverse_forward(self):
        # 可进一步用断言替代 print，确保遍历结果正确
        # …（需要返回列表或提供回调以便断言）
        pass

if __name__ == '__main__':
    unittest.main()
