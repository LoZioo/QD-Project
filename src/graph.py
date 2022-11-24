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

	# def bfs(self, entry_vertex: DirectGraphNode) -> list[DirectGraphNode]:
		# q = Queue[DirectGraphNode]()
	
	def getMatrix(self) -> DirectGraphAdjacencyMatrix:
		return self.__adj_matrix


# Temp code |--------------------------------------------------------

m1 = [
	[0, 1, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 1],
	[0, 0, 0, 1, 0, 0],
	[1, 0, 0, 0, 0, 0],
	[1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
]

n = len(m1)

print("len: %d" % n)

m: DirectGraphAdjacencyMatrix = DirectGraphAdjacencyMatrix()

for i in range(n):
	m.append([])
	
	for j in range(n):
		# m[i][j] = str(m1[i][j])
		# print("i: %d, j: %d" % (i, j))
		m[i][j] = DirectGraphNode(m1[i][j])

# print(m)
