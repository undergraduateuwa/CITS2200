class Node:
    def __init__(self,data):
        self.value  = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.ptr_head = None
        self.ptr_tail = None
        self.size = 0

    def add_first(self, value):
        newNode = Node(value)
        newNode.next = self.ptr_head
        if self.size == 0:
            self.ptr_tail = newNode

        self.ptr_head = newNode
        self.size += 1


    def add_last(self, value):
        newnode = Node(value)
        if self.size == 0:
            self.ptr_head = newnode
            self.ptr_tail = newnode
        else:
            self.ptr_tail.next = newnode
            self.ptr_tail = self.ptr_tail.next

        self.size += 1

    def delete(self):
        if not self.is_empty():
            res = self.ptr_head.value
            self.ptr_head = self.ptr_head.next
            self.size -= 1
            if self.is_empty():
                self.ptr_tail = None
            return res
        else:
            return None


    def traverse(self):
        temp = self.ptr_head
        while temp:
            print(temp.value)
            temp = temp.next

    def is_empty(self):
        return self.size == 0

class linkque:
    def __init__(self):
        self.data = LinkedList()

    def enqueue(self,val):
        self.data.add_last(val)

    def dequeue(self):
        return self.data.delete()

    def is_empty(self):
        return self.data.size == 0

class linkstack:
    def __init__(self):
        self.data = LinkedList()

    def is_empty(self):
        return self.data.size == 0

    def pop(self):
        if not self.is_empty():
            res = self.data.ptr_head.value
            self.data.ptr_head = self.data.ptr_head.next
            self.data.size -= 1
            return res

        return None
    def push(self,val):
        self.data.add_first(val)


    def peek(self):
        if not self.is_empty():
            res = self.data.ptr_head.value
            return res
        else:
            return None




if __name__ == "__main__":
    s = linkstack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top:", s.peek())     # 30
    print("Pop:", s.pop())      # 30
    print("Top:", s.peek())     # 20
    print("Empty?", s.is_empty()) # False
    print("Pop:", s.pop())      # 20
    print("Pop:", s.pop())      # 10
    print("Empty?", s.is_empty()) # True
    print("Pop:", s.pop())      # None

    ll = LinkedList()
    ll.add_last(1)
    ll.add_last(2)
    ll.add_last(3)
    ll.add_last(4)
    ll.add_last(5)
    ll.traverse()








