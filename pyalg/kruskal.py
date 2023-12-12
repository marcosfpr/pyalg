from pyalg.graph import Graph


class Kruskal:
    def __init__(self, graph):
        self.graph = graph
        self.parent = [i for i in range(len(self.graph.adjacency_matrix))]
        self.rank = [0 for _ in range(len(self.graph.adjacency_matrix))]
        self.edges = self.__edges_sorted()

    def __edges_sorted(self):
        n = len(self.graph.adjacency_matrix)
        edges = []
        for u in range(n):
            for v in range(u + 1, n):
                if self.graph.adjacency_matrix[u][v] > 0:
                    edges.append((u, v, self.graph.adjacency_matrix[u][v]))
        edges.sort(key=lambda x: x[2])
        return edges

    def __find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.__find(self.parent[u])
        return self.parent[u]

    def __union(self, u, v):
        u = self.__find(u)
        v = self.__find(v)
        if u == v:
            return
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        elif self.rank[v] < self.rank[u]:
            self.parent[v] = u
        else:
            self.parent[u] = v
            self.rank[v] += 1

    def solve(self):
        total_weight = 0

        mst = []
        for u, v, w in self.edges:
            set_of_u = self.__find(u)
            set_of_v = self.__find(v)
            if set_of_u != set_of_v:
                self.__union(u, v)
                total_weight += w
                mst.append((u, v))
        return mst, total_weight


if __name__ == "__main__":
    m = [
        [0, 8, 9, 0, 10],
        [8, 0, 3, 10, 4],
        [9, 3, 0, 0, 4],
        [0, 10, 0, 0, 7],
        [10, 4, 4, 7, 0],
    ]

    k = Kruskal(Graph(m))
    print(k.graph)
    print(k.solve())
