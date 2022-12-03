from src.graph import DirectGraph
import numpy as np

def test_DirectGraph() -> None:
	# Refers to docs/DirectGraph_example.graphml in https://graphonline.ru/en/
	adj_matr = np.array([
		[0, 1, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 1],
		[0, 0, 0, 1, 0, 0],
		[1, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
	])

	label_arr = np.array(["A", "B", "C", "D", "E", "F"])
	g = DirectGraph(adj_matr, label_arr)

	# ---| label_to_index |---
	for i, label in enumerate(label_arr):
		assert g.label_to_index(label) == i

	assert g.label_to_index("G") == None

	# ---| setEdge |---
	g.setEdge("B", "A")

	# ---| clearEdge |---
	g.clearEdge("B", "A")

	# ---| bfs |---
	assert g.bfs("A") == ["A", "B", "C", "F", "D"]
	assert g.bfs("B") == ["B", "C", "F", "D", "A"]
	assert g.bfs("C") == ["C", "D", "A", "B", "F"]
	assert g.bfs("D") == ["D", "A", "B", "C", "F"]
	assert g.bfs("E") == ["E", "A", "B", "C", "F", "D"]

	# ---| dfs |---
	assert g.dfs("A") == ["A", "B", "C", "D", "F"]
	assert g.dfs("B") == ["B", "C", "D", "A", "F"]
	assert g.dfs("C") == ["C", "D", "A", "B", "F"]
	assert g.dfs("D") == ["D", "A", "B", "C", "F"]
	assert g.dfs("E") == ["E", "A", "B", "C", "D", "F"]
