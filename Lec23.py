import heapq

from Lec19 import graph


class ShortestPath:

    def __init__(self,graph):
        self.graph = graph

    def Dijkstra(self,src):
        dic = {}
        path = {}
        vertex = self.graph.get_vertex()
        for v in vertex:
            dic[v] = float("inf")
            path[v] = None
        dic[src] = 0
        heap_v = [(0,src)]

        while heap_v and len(self.graph.visted) < len(vertex):
            cur_d,v = heapq.heappop(heap_v)
            if cur_d > dic[v] or v in self.graph.visted:
                continue
            self.graph.visted.add(v)
            for key,val in self.graph.adj_map[v].items():
                if key not in self.graph.visted:
                    new_d = cur_d + val
                    if new_d < dic[key]:
                        dic[key] = new_d
                        path[key] = v
                        heapq.heappush(heap_v, (new_d, key))

        self.graph.visted = set()
        return dic, path

    def Bellman_Ford(self):

        verts = self.graph.get_vertex()
        if not verts:
            return {}, {}, False


        src = verts[0]
        dist = {v: float("inf") for v in verts}
        prev = {v: None for v in verts}
        dist[src] = 0


        edges = []
        seen = set()
        for u in verts:
            for v, w in self.graph.adj_map[u].items():
                # 无向图中去掉重复：只保留 (u,v) 中 u<v 的情况
                x, y = (u, v) if u < v else (v, u)
                if (x, y) not in seen:
                    seen.add((x, y))
                    # 对无向图，需要把 (u->v,w) 和 (v->u,w) 都加进边列表
                    edges.append((u, v, w))
                    edges.append((v, u, w))

        # |V|-1 次松弛
        for _ in range(len(verts) - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    updated = True
            # 如果一轮松弛没有任何更新，可以提前退出
            if not updated:
                break

        # 检测是否存在负权回路：再做一次松弛
        has_negative_cycle = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                has_negative_cycle = True
                break

        return dist, prev, has_negative_cycle

    def Floyd_Warshall(self):
        verts = self.graph.get_vertex()
        n = len(verts)
        if n == 0:
            return {}, {}

        # 初始化距离矩阵和 next_hop：
        # dist_matrix[u][v] = ∞ 或 u->v 的权重，若 u=v 则 0
        dist_matrix = {u: {v: float("inf") for v in verts} for u in verts}
        next_hop = {u: {v: None for v in verts} for u in verts}

        for u in verts:
            dist_matrix[u][u] = 0
            next_hop[u][u] = u
            for v, w in self.graph.adj_map[u].items():
                # 对无向图而言，adj_map[u][v] 已经包含 u->v 和 v->u
                dist_matrix[u][v] = w
                next_hop[u][v] = v

        # 三重循环：按中转点 k，不断更新 dist(u,v) = min(dist(u,v), dist(u,k)+dist(k,v))
        for k in verts:
            for i in verts:
                # 如果 i->k 本身不可达，就跳过
                if dist_matrix[i][k] == float("inf"):
                    continue
                for j in verts:
                    if dist_matrix[k][j] == float("inf"):
                        continue
                    new_d = dist_matrix[i][k] + dist_matrix[k][j]
                    if new_d < dist_matrix[i][j]:
                        dist_matrix[i][j] = new_d
                        # 记录从 i 到 j 的路径上，i 的下一跳应该沿 i->k 的路径
                        next_hop[i][j] = next_hop[i][k]

        return dist_matrix, next_hop


if __name__ == "__main__":
    # 构造示例图
    g = graph()
    g = graph()
    g.add_edge(1, 2, 7)
    g.add_edge(1, 3, 9)
    g.add_edge(1, 6, 14)
    g.add_edge(2, 3, 10)
    g.add_edge(2, 4, 15)
    g.add_edge(3, 4, 11)
    g.add_edge(3, 6, 2)
    g.add_edge(4, 5, 6)
    g.add_edge(5, 6, 9)

    sp = ShortestPath(g)

    # 1) 测试 Dijkstra
    dist_dij, prev_dij = sp.Dijkstra(1)
    print("Dijkstra 最短距离:", dist_dij)
    print("Dijkstra 前驱:", prev_dij)

    # 2) 测试 Bellman-Ford
    dist_bf, prev_bf, neg_cycle = sp.Bellman_Ford()
    print("\nBellman-Ford 最短距离:", dist_bf)
    print("Bellman-Ford 前驱:", prev_bf)
    print("是否存在负权回路？", neg_cycle)

    # 3) 测试 Floyd-Warshall
    dist_fw, next_fw = sp.Floyd_Warshall()
    print("\nFloyd-Warshall 距离矩阵:")
    for u in dist_fw:
        print(f"  从 {u} 到其他顶点: {dist_fw[u]}")
    print("Floyd-Warshall 下一跳字典:")
    for u in next_fw:
        print(f"  next_hop[{u}]: {next_fw[u]}")
