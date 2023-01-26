from src.parser import Parser

import networkx as nx
import matplotlib.pyplot as plt

class DirectGraphPrinter:
	# Inizialize graph_to_print and positions.
	def __init__(self, parser: Parser) -> None:
		# Save the parser as a property, so other methods can access it to retrieve data.
		self.parser = parser

	# From the classical indexed adj list (from parser) to a labeled adj list.
	def getLabeledAdjList(self) -> list[tuple[str, str]]:
		label_arr = self.parser.getLabelArray()
		adj_list = self.parser.getAdjList()
		adj_list_labeled: list[tuple[str, str]] = []

		for edge in adj_list:
			adj_list_labeled.append((label_arr[edge[0]], label_arr[edge[1]]))

		return adj_list_labeled

	# Convert the getPositions from parser class to a NetworkX compatible format.
	# {"q1": (321, 147), "q2": (464, 63), "q3": (605, 139), "q4": (465, 220)}
	def getNodePositions(self) -> dict[str, tuple[int, int]]:
		nodes = self.parser.getPositions()
		positions: dict[str, tuple[int, int]] = {}

		for node in nodes:
			positions[node["label"]] = (node["x"], node["y"])

		return positions

	# Print an image of the graph using the functions of the library NetworkX by passing
	# a path through the parameter "path" the image will be saved in the desired location.
	def saveGraph(self, path: str, figsize_x: int = 15, figsize_y: int = 10) -> None:
		networkx_positions = self.getNodePositions()
		graph_to_print = nx.DiGraph()

		graph_to_print.add_nodes_from(self.parser.getLabelArray())
		graph_to_print.add_edges_from(self.getLabeledAdjList())

		plt.figure(figsize = (figsize_x, figsize_y))
		plt.axis("off")

		nx.draw_networkx(
			graph_to_print,
			networkx_positions,
			node_size = 1000,
			font_size = 18,
			node_color = "white",
			edgecolors = "black",
			linewidths = 2,
			width = 2
		)

		# plt.show()
		plt.savefig(path)
