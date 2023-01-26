from src.parser import Parser

import networkx as nx
import matplotlib.pyplot as plt

class DirectGraphPrinter:
	# Inizialize self.graph_to_print and positions.
	def __init__(self, parser: Parser) -> None:
		# Save the parser as a property, so other methods can access it to retrieve data.
		self.parser = parser

		# We need to save this because the class ASFDPrinter will use it to print the ASFD over the graph.
		self.graph_to_print = nx.DiGraph()

	# From the classical indexed adj list (from parser) to a labeled adj list.
	def getLabeledAdjList(self) -> list[tuple[str, str]]:
		label_arr = self.parser.getLabelArray()
		adj_list = self.parser.getAdjList()
		adj_list_labeled: list[tuple[str, str]] = []

		for edge in adj_list:
			adj_list_labeled.append((label_arr[edge[0]], label_arr[edge[1]]))

		return adj_list_labeled

	# Convert the getInfoFromNodes from parser to a NetworkX compatible format.
	# {"q1": (321, 147), "q2": (464, 63), "q3": (605, 139), "q4": (465, 220)}
	def getNodePositions(self) -> dict[str, tuple[int, int]]:
		nodes = self.parser.getInfoFromNodes()
		positions: dict[str, tuple[int, int]] = {}

		for node in nodes:
			positions[node["label"].strip("_")] = (node["posX"], node["posY"])

		return positions

	# Save an image of the graph using the functions of the library NetworkX by passing
	# a path through the parameter "path" the image will be saved in the desired location.
	def saveGraph(self, path: str, save: bool = True) -> None:
		assert path != ""

		networkx_positions = self.getNodePositions()

		self.graph_to_print.add_nodes_from(self.parser.getLabelArray())
		self.graph_to_print.add_edges_from(self.getLabeledAdjList())

		plt.figure(figsize = (15, 10))
		plt.axis("off")

		# Draw nodes.
		nx.draw_networkx(
			self.graph_to_print,
			networkx_positions,
			width = 2,
			linewidths = 2,
			node_size = 1000,
			node_color = "white",
			font_size = 14,
			edgecolors = "black"
		)

		# plt.show()
		if save:
			plt.savefig(path)
