from typing import Tuple

from pyalg.graph import Graph

INF = 10**9


class Prim:
    def __init__(self, graph) -> None:
        self.graph = graph

    def __find_min_unvisited_edge(self, visited) -> Tuple[Tuple[int, int], int]:
        n = len(self.graph.adjacency_matrix)
        min_edge = (-1, -1)
        min_weight = INF
        for u in range(n):
            for v in range(n):
                if (
                    visited[u]
                    and not visited[v]
                    and 0 < self.graph.adjacency_matrix[u][v] < min_weight
                ):
                    min_edge = (u, v)
                    min_weight = self.graph.adjacency_matrix[u][v]
        return (
            min_edge,
            min_weight,
        )

    def solve(self, start=0):
        n = len(self.graph.adjacency_matrix)

        visited = [False for _ in range(n)]
        visited[start] = True
        edges = []
        total_weight = 0

        for _ in range(n - 1):
            min_edge, weight = self.__find_min_unvisited_edge(visited)
            edges.append(min_edge)
            visited[min_edge[1]] = True
            total_weight += weight

        return edges, total_weight


if __name__ == "__main__":
    prim = Prim(Graph.random(5, max_value=10))
    print(prim.graph)
    print(prim.solve(2))
