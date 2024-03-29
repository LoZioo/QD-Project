from src.parser import Parser, Node_t, Edge_t
from include.data_test_ASFD import ASFD_init, DirectGraph_init

import numpy as np

def test_Parser() -> None:
	parser = Parser("docs/Esempio di delta.graphml")

	# getInfoFromNodes.
	nodes: list[Node_t] = [
		{"posX": 321,	"posY": 147,	"node_id": 0,	"label": "_q1"},
		{"posX": 464,	"posY": 63,		"node_id": 1,	"label": "q2"},
		{"posX": 605,	"posY": 139,	"node_id": 2,	"label": "q3_"},
		{"posX": 465,	"posY": 220,	"node_id": 3,	"label": "q4"}
	]

	assert nodes == parser.getInfoFromNodes()

	# getInfoFromEdges.
	edges: list[Edge_t] = [
		{"source_id": 0,	"target_id": 1,	"upText": "a"},
		{"source_id": 1,	"target_id": 2,	"upText": "b"},
		{"source_id": 2,	"target_id": 3,	"upText": "a"},
		{"source_id": 0,	"target_id": 3,	"upText": "b"},
		{"source_id": 3,	"target_id": 3,	"upText": "ab"},
		{"source_id": 1,	"target_id": 1,	"upText": "a"},
		{"source_id": 2,	"target_id": 2,	"upText": "b"}
	]

	assert edges == parser.getInfoFromEdges()

	# getSigma.
	assert ASFD_init.sigma == parser.getSigma()

	# getSigmaNormalized.
	sigma_normalized = list(set(ASFD_init.sigma))
	sigma_normalized.sort()

	assert sigma_normalized == parser.getSigmaNormalized()

	# getEntryState and getFinalStates.
	assert ASFD_init.entry_state == parser.getEntryState()
	assert ASFD_init.final_states == parser.getFinalStates()

	# getLabelArray.
	assert np.array_equal(DirectGraph_init.label_arr, parser.getLabelArray())

	# getAdjMatr.
	assert np.array_equal(DirectGraph_init.adj_matr, parser.getAdjMatr())

	# getAdjList.
	adj_list_expected: list[tuple[int, int]] = []

	for edge in edges:
		adj_list_expected.append((edge["source_id"], edge["target_id"]))

	assert np.array_equal(adj_list_expected, parser.getAdjList())

	# getDelta.
	assert np.array_equal(ASFD_init.delta, parser.getDelta())
