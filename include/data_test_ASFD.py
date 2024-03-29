from src.graph import DirectGraph_init_t
from src.ASFD import ASFD_init_t

import numpy as np

# Refers to docs/Esempio di delta.png
DirectGraph_init = DirectGraph_init_t(
	adj_matr = np.array([
		[0, 1, 0, 1],
		[0, 1, 1, 0],
		[0, 0, 1, 1],
		[0, 0, 0, 1],
	]),

	label_arr = np.array(["q1", "q2", "q3", "q4"])
)

ASFD_init = ASFD_init_t(
	sigma = "abababab",

	delta = np.array([
#		qi  'a'   'b'
		["q2", "q4"],		# delta(q1, a) = q2 AND delta(q1, b) = q4.
		["q2", "q3"],		# delta(q2, a) = q2 AND delta(q2, b) = q3.
		["q4", "q3"],		# delta(q3, a) = q4 AND delta(q3, b) = q3.
		["q4", "q4"],		# delta(q4, a) = q4 AND delta(q4, b) = q4.
	]),

	entry_state = "q1",
	final_states = {"q3"}
)
