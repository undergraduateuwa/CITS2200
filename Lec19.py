from collections import deque


class graph:

    def __init__(self):
        self.adj_map = {}
        self.visted = set()

    def add_vertex(self,id):
        if id not in self.adj_map.keys():
            self.adj_map[id] = {}
    def add_edge(self,src,des,weight):
        self.add_vertex(src)
        self.add_vertex(des)

        self.adj_map[src][des] = weight
        self.adj_map[des][src] = weight

    def get_vertex(self):
        return list(self.adj_map.keys())

    def get_neighbors(self,v):
        return list(self.adj_map.get(v,{}).keys())

    def __repr__(self):
        return "\n".join(f"{v}: {nbrs}" for v, nbrs in self.adj_map.items())


    def BFs(self, vid: object) -> object:
        res = []
        if vid in self.adj_map.keys():
            queue = deque([vid])
            res.append(vid)
            self.visted.add(vid)
            while queue:
                cur = queue.popleft()
                sinlings = self.get_neighbors(cur)
                for items in sinlings :
                    if items not in self.visted:
                        res.append(items)
                        queue.append(items)
                        self.visted.add(items)
        self.visted = set()
        return res
    def DFs(self, vid, res) :
        res.append(vid)
        self.visted.add(vid)
        for items in self.get_neighbors(vid):
            if items not in self.visted:
                self.DFs(items, res)




if __name__ == "__main__":
    g = graph()
    g.add_edge("A", "B", 3)
    g.add_edge("A", "C", 2)
    g.add_edge("A", "D", 5)
    g.add_edge("B", "C", 5)
    g.add_edge("B", "E", 5)
    g.add_edge("E", "C", 5)
    res = []
    g.DFs("A",res)
    print(res)

