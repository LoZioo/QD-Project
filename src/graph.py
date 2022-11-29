import numpy as np
import numpy.typing as npt

from src.queue import Queue

# Classes |----------------------------------------------------------

class DirectGraph:
	__adj_matrix:		npt.NDArray[np.uint8]
	__label_matrix:	npt.NDArray[np.string_]

	def __init__(self, adj_matrix: npt.NDArray[np.uint8], label_matrix: npt.NDArray[np.string_]) -> None:
		# ---| adj_matrix |---
		assert len(adj_matrix) > 0

		# Must be a square matrix.
		assert len(adj_matr.shape) == 2
		assert adj_matr.shape[0] == adj_matr.shape[1]

		# ---| label_matrix |---
		assert len(label_matrix) == len(adj_matr)

		
		self.__adj_matrix = adj_matrix.copy()
		self.__label_matrix = label_matrix.copy()

	def bfs(self, entry_vertex: str) -> npt.NDArray[np.string_]:
		# ---| IndexError |---
		entry_vertex_index = np.where(self.__label_matrix == entry_vertex)[0]
		
		assert len(entry_vertex_index) == 1
		entry_vertex_index = entry_vertex_index[0]
		
		# print("-----")
		# print(entry_vertex_index)
		# print("-----")

		# SCRIVERE CODICE

		# ---| Code |---
		q = Queue[str]()

		return np.array(q)
	
	def get(self) -> tuple[npt.NDArray[np.uint8], npt.NDArray[np.string_]]:
		return (self.__adj_matrix.view(), self.__label_matrix.view())


# Temp code |--------------------------------------------------------

print("\n")

adj_matr = np.array([
	[0, 1, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 1],
	[0, 0, 0, 1, 0, 0],
	[1, 0, 0, 0, 0, 0],
	[1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
])

label_matrix = np.array(["1", "2", "3", "4", "5", "6"])

g = DirectGraph(adj_matr, label_matrix)
g.bfs("1")
