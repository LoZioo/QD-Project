from src.parser import Parser
from include.data_test_ASFD import ASFD_init, DirectGraph_init
from src.parser import Node_t, Edge_t

import numpy as np

def test_Parser() -> None:
	parser = Parser("docs/Esempio di delta.graphml")

	# test for getInfoFromNodes

	firstNode : Node_t = {'posX': 321, 'posY': 147, 'node_id': 0, 'label': '_q1'}
	secondNode : Node_t = {'posX': 464, 'posY': 63, 'node_id': 1, 'label': 'q2'}
	thirdNode : Node_t = {'posX': 605, 'posY': 139, 'node_id': 2, 'label': 'q3_'}
	fourthNode : Node_t = {'posX': 465, 'posY': 220, 'node_id': 3, 'label': 'q4'}

	nodes: list[Node_t] = [firstNode, secondNode, thirdNode, fourthNode]

	nodesParser: list[Node_t] = parser.getInfoFromNodes()

	assert np.array_equal(nodes, nodesParser)

	# test for getPositions

	positions: list[tuple[int, int]] = [(321, 147), (464, 63), (605, 139), (465, 220)]

	positionsParser: list[tuple[int, int]] = parser.getPositions()

	assert np.array_equal(positions, positionsParser)

	# test for getEntryState and getFinalStates

	entryState: str = "q1"
	finalStates: set[str] = {'q3'}

	entryStateParsing: str = parser.getEntryState()
	finalStatesParsing: set[str] = parser.getFinalStates()

	assert entryState == entryStateParsing
	assert np.array_equal(finalStates, finalStatesParsing)

	# test for getLabelArray

	labelArray: npt.NDArray[np.string_] = ["q1", "q2", "q3", "q4"]

	labelArrayParsing: npt.NDArray[np.string_] = parser.getLabelArray()

	assert np.array_equal(labelArray, labelArrayParsing)

'''
	print("\ngetInfoFromEdges:")
	for edge in parser.getInfoFromEdges():
		print(edge)

	print()
	print("getSigma: %s" % parser.getSigma())
	
	

	print("\ngetAdjMatr")
	print(parser.getAdjMatr())
	
	print("\ngetDelta")
	print(parser.getDelta())
'''