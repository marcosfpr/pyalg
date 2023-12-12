import random
from dataclasses import dataclass
from typing import List


@dataclass
class Graph:
    adjacency_matrix: List[List[int]]

    @staticmethod
    def zeros(n) -> "Graph":
        return Graph([[0 for _ in range(n)] for _ in range(n)])

    @staticmethod
    def random(n, max_value=100) -> "Graph":
        graph = Graph.zeros(n)

        for i in range(n):
            for j in range(i + 1, n):
                graph.adjacency_matrix[i][j] = graph.adjacency_matrix[j][
                    i
                ] = random.randint(0, max_value)

        return graph

    def __str__(self):
        return "\n".join(map(str, self.adjacency_matrix))
