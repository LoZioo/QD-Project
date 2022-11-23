from typing import NewType, Union
from src.queue import Queue

# Types |------------------------------------------------------------

# Node label.
DirectGraphNode = str
DirectGraphAdjacencyMatrix = NewType("GraphAdjacencyMatrix", list[list[DirectGraphNode]])

# Classes |----------------------------------------------------------

class DirectGraph:
	__adj_matrix:	DirectGraphAdjacencyMatrix

	def __init__(self, adj_matrix: DirectGraphAdjacencyMatrix) -> None:
		assert len(adj_matrix) > 0
		assert len(adj_matrix) == len(adj_matrix[0])

		self.__adj_matrix = adj_matrix

	def bfs(self, entry_vertex: DirectGraphNode) -> list[DirectGraphNode]:
		q = Queue[DirectGraphNode]()
