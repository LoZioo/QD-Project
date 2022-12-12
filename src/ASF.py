from src.graph import DirectGraph, DirectGraph_init_t

from typing import NamedTuple

import numpy as np
import numpy.typing as npt

# From formal definition to code:
# sigma:									Sigma
# DirectGraph.label_arr:	Q
# delta:									delta
# entry_state:						q0
# final_states:						F

class ASF_init_t(NamedTuple):
	sigma:				str
	delta:				npt.NDArray[np.string_]		# Matrix; dimensions |Q| x |Sigma|.
	entry_state:	str
	final_states:	set[str]									# Set; max len = |Q|

class ASF(DirectGraph):
	sigma:				set[str]
	delta_matr:		npt.NDArray[np.string_]		# Merge between DirectGraph.label_arr and DirectGraph.adj_matr.
	entry_state:	str
	final_states:	set[str]

	def __init__(self, ASF_init: ASF_init_t, DirectGraph_init: DirectGraph_init_t) -> None:
		super().__init__(DirectGraph_init)

		# AGGIUNGERE assert() !!!
		
		self.sigma = { c for c in ASF_init.sigma }
		self.entry_state = ASF_init.entry_state
		self.final_states = ASF_init.final_states.copy()

		n = len(DirectGraph_init.adj_matr)	# |Q|, number of states.
		self.delta_matr = np.full((n, n), "")
		
		for i, u in enumerate(DirectGraph.adj_matr):
			for j, v in enumerate(u):
				pass
				# self.delta_matr[i][j] += "a"	# CREARE MATRICE DI ADIACENZA EFFETTIVA (Vedi "Esempio di delta.png").
