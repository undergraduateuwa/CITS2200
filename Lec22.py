import heapq

from Lec19 import graph
class MSTree:

    def __init__(self,graph):
        self.graph = graph
        self.edges = []
        seen = set()
        vertexs = self.graph.get_vertex()
        for src in vertexs:
            seen.add(src)
            for des in self.graph.adj_map[src].keys():
                if des not in seen:
                    self.edges.append([src, des, self.graph.adj_map[src][des]])
        self.edges.sort(key=lambda x: x[2], reverse=True)

    def kruskal(self):
        unf = unifind(self.graph)
        res = graph()

        while len(self.edges) > 0:
            miniweight = self.edges.pop()
            if unf.find(miniweight[0]) != unf.find(miniweight[1]):
                res.add_edge(miniweight[0],miniweight[1],miniweight[2])
                unf.union(miniweight[0],miniweight[1])
        return res


    def prim(self,num):
        res = graph()
        edge_heap = []
        vetex = self.graph.get_vertex()
        start = vetex[num]
        self.graph.visted.add(start)
        for out,w in self.graph.adj_map[start].items():
            heapq.heappush(edge_heap, (w, start, out))

        while edge_heap and len(self.graph.visted):
            w, u, v = heapq.heappop(edge_heap)
            if v in self.graph.visted:
                continue

            res.add_edge(u, v, w)
            self.graph.visted.add(v)
            for to, w2 in self.graph.adj_map[v].items():
                if to not in self.graph.visted:
                    heapq.heappush(edge_heap, (w2, v, to))
        self.graph.visted = set()
        return res
class unifind:

    def __init__(self,graph = None):
        self.p = {}
        self.rank = {}
        if graph:
            vertexs = graph.get_vertex()
            for v in vertexs:
                self.p[v] = v
                self.rank[v] = 0

    def find(self,e):
        if self.p[e] != e:
            self.p[e]=self.find(self.p[e])
        return self.p[e]


    def union(self,u,v):
        pu  = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return
        else:
            if self.rank[pu] > self.rank[pv]:
                self.p[pv] = pu
            elif self.rank[pu] < self.rank[pv]:
                self.p[pu] = pv
            else:
                self.p[pu] = pv
                self.rank[pu]+=1

def main():
    g = graph()
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 4, 3)

    print("原图：")
    print(g)
    print("-" * 40)

    # 用 Prim 生成 MST
    primer = MSTree(g)
    mst = primer.prim(0)

    print("Prim 算法生成的 MST：")
    print(mst)
    print("-" * 40)

    # 列出 MST 中所有边，按 weight 排序，方便比对
    mst_edges = []
    seen = set()
    for u in mst.get_vertex():
        for v, w in mst.adj_map[u].items():
            x, y = (u, v) if u < v else (v, u)
            if (x, y) not in seen:
                seen.add((x, y))
                mst_edges.append((x, y, w))

    mst_edges.sort(key=lambda e: e[2])  # 按权重从小到大
    print("MST 的边集 (按权重排序)：")
    for u, v, w in mst_edges:
        print(f"  ({u}, {v}, {w})")

    # 期望结果：[(1,2,1), (2,3,2), (3,4,3)]
    expected = [(1, 2, 1), (2, 3, 2), (3, 4, 3)]
    print("期望的 MST 边集：", expected)
    print("计算得到的 MST 边集：", mst_edges)
    print("测试通过：" if mst_edges == expected else "测试失败！")

if __name__ == "__main__":
    main()