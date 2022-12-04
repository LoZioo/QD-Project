from src.ASF import ASF_init_t

import numpy as np

def test_ASF() -> None:
	a = ASF_init_t(
		sigma = "abcdefghijklmnopqrstuvwxyz",
		entry_state = "q0",
		final_states = np.array(["q1"])
	)

	print(a)
