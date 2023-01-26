from src.parser import Parser
from src.DirectGraph_printer import DirectGraphPrinter

import networkx as nx
import matplotlib.pyplot as plt

class ASFDPrinter(DirectGraphPrinter):
	def __init__(self, parser: Parser) -> None:
		# Call the constructor of the class DirectGraphPrinter.
		super().__init__(parser)
		self.parser = parser

	# Convert the getInfoFromEdges from parser to a NetworkX compatible format.
	# {("q1", "q2"): "a", ("q2", "q3"): "b", ("q3", "q4"): "a", ("q1", "q4"): "b", ("q4", "q4"): "ab", ("q2", "q2"): "a", ("q3", "q3"): "b"}
	def getEdgeTransitions(self) -> dict[tuple[str, str], str]:
		label_arr = self.parser.getLabelArray()
		edges = self.parser.getInfoFromEdges()
		transitions: dict[tuple[str, str], str] = {}

		for edge in edges:
			transitions[ (label_arr[edge["source_id"]], label_arr[edge["target_id"]]) ] = edge["upText"]

		return transitions

	# Save an image of the ASFD using the functions of the library NetworkX by passing
	# a path through the parameter "path" the image will be saved in the desired location.
	def saveASFD(self, path: str, save: bool = True) -> None:
		assert path != ""

		# Initialize self.graph_to_print, but do not save the results.
		self.saveGraph(path, False)
		networkx_positions = self.getNodePositions()

		# The entry_state is printed in red.
		nx.draw_networkx_nodes(
			self.graph_to_print,
			networkx_positions,
			node_size = 1000,
			nodelist = { self.parser.getEntryState() },
			node_color = "tab:red",
			alpha = 0.5,
			edgecolors = "black"
		)

		# The final_states are printed in green.
		nx.draw_networkx_nodes(
			self.graph_to_print,
			networkx_positions,
			node_size = 1000,
			nodelist = self.parser.getFinalStates(),
			node_color = "tab:green",
			alpha = 0.5,
			edgecolors = "black"
		)

		# Shift positions for a better visualisation of edge labels.
		networkx_transitions: dict[str, tuple[int, int]] = {}
		for position in networkx_positions.items():
			networkx_transitions[position[0]] = (networkx_positions[position[0]][0], networkx_positions[position[0]][1] + 8)

		# Draw transitions.
		nx.draw_networkx_edge_labels(
			self.graph_to_print,
			networkx_transitions,
			edge_labels = self.getEdgeTransitions(),
			label_pos = 0.5,
			font_size = 12,
			font_color = "blue"
		)

		# plt.show()
		if save:
			plt.savefig(path)
