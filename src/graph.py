from typing import Union

import numpy as np
import numpy.typing as npt

from src.queue import Queue

# Classes |----------------------------------------------------------
class DirectGraph:
	__adj_matr:	npt.NDArray[np.uint8]
	__label_arr:	npt.NDArray[np.string_]

	def __label_to_index(self, label: str) -> Union[int, None]:
		# ---| IndexError |---
		vertex_search_results = np.where(self.__label_arr == label)[0]

		# One and only one vertex must be found.
		if len(vertex_search_results) == 1:
			return vertex_search_results[0]

		return None

	def __init__(self, adj_matr: npt.NDArray[np.uint8], label_arr: npt.NDArray[np.string_]) -> None:
		# ---| adj_matr |---
		assert len(adj_matr) > 0

		# Must be a square matrix.
		assert len(adj_matr.shape) == 2
		assert adj_matr.shape[0] == adj_matr.shape[1]

		# ---| label_arr |---
		assert len(label_arr) == len(adj_matr)

		self.__adj_matr = adj_matr.copy()
		self.__label_arr = label_arr.copy()

	def bfs(self, entry_vertex_label: str) -> list[str]:
		# ---| __label_to_index error |---
		entry_vertex_index = self.__label_to_index(entry_vertex_label)
		assert entry_vertex_index is not None

		# ---| Code |---
		n = len(self.__adj_matr)

		q = Queue[int]()
		visited = np.full(n, False)
		res = list[str]()

		q.enque(entry_vertex_index)
		visited[entry_vertex_index] = True

		while not q.isEmpty():
			v_index = q.deque()
			visited[v_index] = True

			# Append current node to the results list.
			res.append(str(self.__label_arr[v_index]))

			# For iteration with x item and i index.
			for i, x in enumerate(self.__adj_matr[v_index]):
				# if x is an unvisited neighbour:
				if x == 1 and not visited[i]:
					q.enque(i)

		return res

	def get(self) -> tuple[npt.NDArray[np.uint8], npt.NDArray[np.string_]]:
		return (self.__adj_matr.view(), self.__label_arr.view())
