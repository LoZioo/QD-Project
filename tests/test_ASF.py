from src.graph import DirectGraph_init_t
from src.ASF import ASF, ASF_init_t

import numpy as np

def test_ASF() -> None:
	DirectGraph_init = DirectGraph_init_t(
		adj_matr = np.array([
			[0, 1, 0, 1],
			[0, 1, 1, 0],
			[0, 0, 1, 1],
			[0, 0, 0, 1],
		]),

		label_arr = np.array(["q1", "q2", "q3", "q4"])
	)

	ASF_init = ASF_init_t(
		sigma = "ab",

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

	asf = ASF(ASF_init, DirectGraph_init)

	print(asf.final_states)
