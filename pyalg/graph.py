import random
from dataclasses import dataclass
from typing import List

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


@dataclass
class Graph:
    adjacency_matrix: List[List[int]]

    def to_numpy(self):
        return np.array(self.adjacency_matrix)

    def plot(self):
        graph = nx.from_numpy_array(self.to_numpy())
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos=pos, with_labels=True)
        labels = nx.get_edge_attributes(graph, "weight")
        nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=labels)
        plt.show()

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
