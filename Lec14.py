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


if __name__ == "__main__":
    dl = doulelink()

    print("Is empty?", dl.is_empty())  # True

    n1 = dl.insert_btw(dl.ptr_head, dl.ptr_tail, 10)
    n2 = dl.insert_btw(n1, dl.ptr_tail, 20)
    n3 = dl.insert_btw(n2, dl.ptr_tail, 30)

    print("Traverse forward:")
    dl.traverse_forward()  # 10 20 30

    print("Traverse backward:")
    dl.traverse_back()     # 30 20 10

    print("Length:", dl.len())  # 3

    print("Deleting 20")
    dl.delete(n2)

    print("Traverse forward after deletion:")
    dl.traverse_forward()  # 10 30

    print("Traverse backward after deletion:")
    dl.traverse_back()     # 30 10

    print("Length:", dl.len())  # 2

    print("Is empty?", dl.is_empty())  # False

    dl.delete(n1)
    dl.delete(n3)
    print("Is empty after all deletions?", dl.is_empty())  # True

