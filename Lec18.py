class MiniHeap:
    def __init__(self):
        self.data = []
        self.size = 0

    def insert(self,val):
        self.data.append(val)
        self.up(len(self.data)-1)
        self.size += 1

    def up(self,idx):
        while (idx-1)//2 >= 0:
            if self.data[idx] < self.data[(idx-1)//2]:
                self.swap(idx, (idx - 1) // 2)
                idx = (idx - 1) // 2
            else:
                break
    def delete(self):
        self.swap(0,-1)
        res = self.data.pop()
        self.size -= 1
        self.down(0)
        return res

    def down(self,idx):
        while idx * 2 + 1 < self.size:
            small = idx
            l = idx * 2 + 1
            r = idx * 2 + 2
            if self.data[l] < self.data[small]:
                small = l
            if r < self.size and self.data[r] < self.data[small]:
                small = r
            if small != idx:
                self.swap(idx,small)
                idx = small
            else:
                break


    def swap(self,a,b):
        temp = self.data[a]
        self.data[a] = self.data[b]
        self.data[b] = temp

    def MiniHeap_sort(self):
        while self.size > 0:
            self.swap(0,self.size-1)
            self.size -= 1
            self.down(0)
        self.size = len(self.data)

    def heapify(self,arr):
        self.size = len(arr)
        self.data = arr
        for i in range((self.size - 2) // 2, -1, -1):  # index 从 (n//2)-1 到 0
            self.down(i)

    def select_sort(self):

        pass

h = MiniHeap()
h.heapify([5, 3, 7, 1, 9])

print("After insert:", h.data)

h.MiniHeap_sort()
print("After sort:", h.data,h.size)
print("Delete:", h.delete())  
print("Heap after delete:", h.data)