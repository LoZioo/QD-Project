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
	def saveASFD(self, path: str, figsize_x: int = 15, figsize_y: int = 10) -> None:
		networkx_positions = self.getNodePositions()
		graph_to_print = nx.DiGraph()

		graph_to_print.add_nodes_from(self.parser.getLabelArray())
		graph_to_print.add_edges_from(self.getLabeledAdjList())

		plt.figure(figsize = (figsize_x, figsize_y))
		plt.axis("off")

		# Draw nodes.
		nx.draw_networkx(
			graph_to_print,
			networkx_positions,
			width = 2,
			linewidths = 2,
			node_size = 1000,
			node_color = "white",
			font_size = 16,
			edgecolors = "black",
			labels = { node: node for node in self.parser.getLabelArray() }
		)

		# The entry_state is printed in red.
		nx.draw_networkx_nodes(
			graph_to_print,
			networkx_positions,
			node_size = 1000,
			nodelist = { self.parser.getEntryState() },
			node_color = "tab:red",
			alpha = 0.2,
			edgecolors = "black"
		)

		# The final_states are printed in green.
		nx.draw_networkx_nodes(
			graph_to_print,
			networkx_positions,
			node_size = 1000,
			nodelist = self.parser.getFinalStates(),
			node_color = "tab:green",
			alpha = 0.2,
			edgecolors = "black"
		)

		# Shift positions for a better visualisation of edge labels.
		edge_labels_pos: dict[str, tuple[int, int]] = {}
		for position in networkx_positions:
			edge_labels_pos[position] = (networkx_positions[position][0], networkx_positions[position][1] + 8)

		# Draw transitions.
		nx.draw_networkx_edge_labels(
			graph_to_print,
			edge_labels_pos,
			edge_labels = self.getEdgeTransitions(),
			label_pos = 0.5,
			font_size = 12,
			font_color = "blue",
			alpha = 0.8,
		)

		# plt.show()
		plt.savefig(path)
