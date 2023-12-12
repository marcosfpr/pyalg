from pyalg.graph import Graph


class HamiltonianPath:
    def __init__(self, graph):
        self.graph = graph
        self.path = []
        self.visited = [False for _ in range(len(self.graph.adjacency_matrix))]

    def solve(self):
        self.__solve(0)
        return self.path

    def is_solved(self):
        return len(self.path) == len(self.graph.adjacency_matrix)

    def __solve(self, u):
        self.visited[u] = True
        self.path.append(u)

        if self.is_solved():
            return True

        for v in range(len(self.graph.adjacency_matrix)):
            if not self.visited[v] and self.graph.adjacency_matrix[u][v] > 0:
                if self.__solve(v):
                    return True
        self.path.pop()
        self.visited[u] = False
        return False


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ]
    graph = Graph(graph)
    print(graph)
    hamiltonian = HamiltonianPath(graph)
    print("Path:", hamiltonian.solve())
