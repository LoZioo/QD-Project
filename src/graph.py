from typing import NewType, Literal

# Direct graph adjacency matrix type.
DirectGraphAdjacencyMatrix = NewType("GraphAdjacencyMatrix", list[list[Literal[0, 1]]])

# Graph class.
class DirectGraph:
	__adj_matrix:		DirectGraphAdjacencyMatrix
	__entry_vertex:	int

	def __init__(self, adj_matrix: DirectGraphAdjacencyMatrix, entry_vertex: int = 0) -> None:
		assert len(adj_matrix) > 0
		assert len(adj_matrix) == len(adj_matrix[0])
		assert entry_vertex >= 0 and entry_vertex < len(adj_matrix) - 1

		self.__adj_matrix = adj_matrix
		self.__entry_vertex = entry_vertex
	
	def bfs(self, entry_vertex: int = 0) -> None:
