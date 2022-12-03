from typing import Union

import numpy as np
import numpy.typing as npt

from src.queue import Queue
from src.stack import Stack

# Classes |----------------------------------------------------------

class DirectGraph:
	# ---| Logical private attributes and methods |---
	adj_matr:		npt.NDArray[np.uint8]
	label_arr:	npt.NDArray[np.string_]

	def label_to_index(self, label: str) -> Union[int, None]:
		vertex_search_results = np.where(self.label_arr == label)[0]

		# One and only one vertex must be found.
		if len(vertex_search_results) == 1:
			return vertex_search_results[0]

		return None

	# ---| Logical public attributes and methods |---
	def __init__(self, adj_matr: npt.NDArray[np.uint8], label_arr: npt.NDArray[np.string_]) -> None:
		# ---| adj_matr |---
		assert len(adj_matr) > 0

		# Must be a square matrix.
		assert len(adj_matr.shape) == 2
		assert adj_matr.shape[0] == adj_matr.shape[1]

		# ---| label_arr |---
		assert len(label_arr) == len(adj_matr)

		self.adj_matr = adj_matr.copy()
		self.label_arr = label_arr.copy()

	def bfs(self, entry_vertex_label: str) -> list[str]:
		# ---| label_to_index error handling |---
		entry_vertex_index = self.label_to_index(entry_vertex_label)
		assert entry_vertex_index is not None

		# ---| Code |---
		n = len(self.adj_matr)

		q = Queue[int]()
		visited = np.full(n, False)
		res = list[str]()

		q.enque(entry_vertex_index)
		while not q.empty():
			v = q.deque()
			visited[v] = True

			# Append current node to the results list.
			res.append(str(self.label_arr[v]))

			# For iteration with w item and i index.
			for i, w in enumerate(self.adj_matr[v]):
				# if w is an unvisited neighbour:
				if w == 1 and not visited[i]:
					q.enque(i)

		return res

	def dfs(self, entry_vertex_label: str) -> list[str]:
		# ---| label_to_index error handling |---
		entry_vertex_index = self.label_to_index(entry_vertex_label)
		assert entry_vertex_index is not None

		# ---| Code |---
		n = len(self.adj_matr)

		s = Stack[int]()
		visited = np.full(n, False)
		res = list[str]()

		s.push(entry_vertex_index)
		while not s.empty():
			v = s.pop()

			if not visited[v]:
				visited[v] = True

				# Append current node to the results list.
				res.append(str(self.label_arr[v]))

			# Array must be evaluated from the end!
			neighbours = np.flip(self.adj_matr[v])

			# For iteration with w item and i index.
			for j, w in enumerate(neighbours):
				i = n - j - 1

				# if w is an unvisited neighbour:
				if w == 1 and not visited[i]:
					s.push(i)

		return res
