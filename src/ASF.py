from src.graph import DirectGraph

from typing import NamedTuple

import numpy as np
import numpy.typing as npt

class ASF_init_t(NamedTuple):
	sigma:				str
	states:				npt.NDArray[np.string_]		# DirectGraph label_arr.
	
	# COME RAPPRESENTO DELTA???
	
	entry_state:	str
	final_states:	npt.NDArray[np.string_]

class ASF(DirectGraph):
	sigma:				set[str]
	entry_state:	str
	final_states:	npt.NDArray[np.string_]

	def __init__(self, init: ASF_init_t) -> None:
		# super().__init__()
		# COME RAPPRESENTO DELTA???
		
		self.sigma = { c for c in init.sigma }
		self.entry_state = init.entry_state
		self.final_states = init.final_states.copy()
