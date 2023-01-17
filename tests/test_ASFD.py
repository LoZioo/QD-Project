from include.data_test_ASFD import DirectGraph_init, ASFD_init
from src.ASFD import ASFD

import numpy as np

def test_ASFD() -> None:
	asfd = ASFD(ASFD_init, DirectGraph_init)

	tests =		np.array(["a", "aa", "ab", "aab", "aabb", "aba", "abab", "ababa", "bab", "baa", "bbb", "aaa", "abbbb", "abb"])
	results =	np.array([False, False, True, True, True, False, False, False, False, False, False, False, True, True])

	for i in range(len(tests)):
		assert asfd.evaluate(tests[i]) == results[i]
