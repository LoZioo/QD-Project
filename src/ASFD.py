from src.graph import DirectGraph, DirectGraph_init_t

from typing import NamedTuple, Any

import numpy as np
import numpy.typing as npt

# From formal definition to code:
# sigma:									Sigma
# DirectGraph.label_arr:	Q
# delta:									delta
# entry_state:						q0
# final_states:						F

class ASFD_init_t(NamedTuple):
	sigma:				str
	delta:				npt.NDArray[np.string_]		# Matrix; |Q| x |Sigma|.
	entry_state:	str
	final_states:	set[str]									# Max len: |Q|.

class ASFD(DirectGraph):
	sigma:				npt.NDArray[np.string_]

	# Merge between ASFD_init_t.delta and DirectGraph.adj_matr; dimensions |Q| x |Q|.
	# Single element: S subseteq of Sigma s.t. |S| <= |Sigma|.
	delta_matr:		npt.NDArray[Any]

	entry_state:	int
	final_states:	set[int]

	def __init__(self, ASFD_init: ASFD_init_t, DirectGraph_init: DirectGraph_init_t) -> None:
		# Q: init DirectGraph superclass.
		super().__init__(DirectGraph_init)

		# Sigma: from string to array of unuque chars (to implement an ordered set).
		assert len(ASFD_init.sigma) > 0
		self.sigma = np.unique(list(ASFD_init.sigma))

		# q0: from string to index.
		assert ASFD_init.entry_state in DirectGraph_init.label_arr
		res = np.where(DirectGraph_init.label_arr == ASFD_init.entry_state)[0]

		assert len(res) == 1
		self.entry_state = res[0]

		# F: from string to indexes.
		assert len(ASFD_init.final_states) <= len(DirectGraph_init.label_arr)
		assert (e in DirectGraph_init.label_arr for e in ASFD_init.final_states)
		self.final_states = { np.where(DirectGraph_init.label_arr == e)[0][0] for e in ASFD_init.final_states }

		# delta: check if delta is defined for every couple (q x c).
		assert ASFD_init.delta.shape == (len(DirectGraph_init.label_arr), len(self.sigma))
		assert ((q in DirectGraph_init.label_arr for q in row) for row in ASFD_init.delta)

		# delta: merging between delta and adj_matr.
		n = len(DirectGraph_init.adj_matr)			# |Q|.
		self.delta_matr = np.full((n, n), {})

		for i, u in enumerate(DirectGraph_init.adj_matr):
			for j, v in enumerate(u):
				if v == 1:
					transitions = np.where(ASFD_init.delta[i] == DirectGraph_init.label_arr[j])[0]
					transitions = { self.sigma[k] for k in transitions }

					self.delta_matr[i][j] = transitions

	def evaluate(self, x: str) -> bool:
		q = self.entry_state
		n = len(x)
		i = 0

		while i < n:
			for j, s in enumerate(self.delta_matr[q]):
				if x[i] in s:
					q = j

			i += 1

		return q in self.final_states
