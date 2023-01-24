import xml.etree.ElementTree as ET					# xml.etree.ElementTree module implements an API for parsing and creating XML data.

from typing import TypedDict

import numpy as np
import numpy.typing as npt

class Node_t(TypedDict):
	posX:			int
	posY:			int
	node_id:	int
	label:		str

class Edge_t(TypedDict):
	source_id:	int
	target_id:	int
	upText:			str

class Positions_t(TypedDict):
	label:	str
	x:			int
	y:			int

class Parser:
	# Constructor.
	def __init__(self, pathname: str) -> None:
		# assert pathname[len(pathname)-8 : len(pathname)] == ".graphml"
		assert pathname[-8:] == ".graphml"

		# XML tree root.
		XML_tree = ET.parse(pathname)
		self.root = XML_tree.getroot()

		# Buffer properties.
		self.nodes_buffer = None
		self.edges_buffer = None

	# General methods.
	def getInfoFromNodes(self) -> list[Node_t]:
		if self.nodes_buffer is not None:
			return self.nodes_buffer

		nodes: list[Node_t] = []

		for item in self.root.findall(".//graph/node"):
			node: Node_t = {
				"posX":			int(float(item.attrib["positionX"])),
				"posY":			int(float(item.attrib["positionY"])),
				"node_id":	int(item.attrib["id"]),
				"label":		item.attrib["mainText"]
			}
			nodes.append(node)

		self.nodes_buffer = nodes
		return nodes

	def getInfoFromEdges(self) -> list[Edge_t]:
		if self.edges_buffer is not None:
			return self.edges_buffer

		edges: list[Edge_t] = []

		for item in self.root.findall(".//graph/edge"):
			edge: Edge_t = {
				"source_id":	int(item.attrib["source"]),
				"target_id":	int(item.attrib["target"]),
				"upText":			item.attrib["upText"]
			}
			edges.append(edge)

		self.edges_buffer = edges
		return edges

	# Derivated methods.
	def getPositions(self) -> list[Positions_t]:
		nodes = self.getInfoFromNodes()
		positions: list[Positions_t] = []

		for node in nodes:
			position: Positions_t = {
				"label":	node["label"].strip("_"),
				"x":			node["posX"],
				"y":			node["posY"],
			}

			positions.append(position)

		return positions

	def getSigma(self) -> str:
		edges = self.getInfoFromEdges()
		sigma: str = ""

		for	edge in edges:
			sigma += edge["upText"]

		return sigma

	def getEntryState(self) -> str:
		nodes = self.getInfoFromNodes()

		entry_state:	str = ""
		label:				str

		for node in nodes:
			label = node["label"]

			if label[0] == "_":
				# entry_state = label[1 : len(label)]
				entry_state = label[1:]

		assert entry_state != ""
		return entry_state

	def getFinalStates(self) -> set[str]:
		nodes = self.getInfoFromNodes()

		final_states:	set[str] = set()
		label:				str

		for node in nodes:
			label = node["label"]

			# if label[len(label)-1] == "_":
			if label[-1] == "_":
				# label = label[0 : len(label)-1]
				label = label[:-1]
				final_states.add(label)

		# assert final_states != {}
		assert final_states
		return final_states

	def getLabelArray(self) -> npt.NDArray[np.string_]:
		nodes = self.getInfoFromNodes()

		label_arr:	list[str] = []
		label:			str = ""

		for node in nodes:
			label = node["label"]

			if label[0] == "_":
				label = label[1 : len(label)]

			if label[len(label)-1] == "_":
				label = label[0 : len(label)-1]

			label_arr.append(label)

		label_arr.sort()
		return np.array(label_arr)

	def getAdjMatr(self) -> npt.NDArray[np.uint8]:
		nodes = self.getInfoFromNodes()
		edges = self.getInfoFromEdges()

		adj_matr = np.zeros((len(nodes), len(nodes)), np.uint8)		# Create an adj_matr full of zeros.

		for edge in edges:
			i = edge["source_id"]
			j = edge["target_id"]

			adj_matr[i][j] = 1

		return adj_matr

	def getAdjList(self) -> list[tuple[int, int]]:
		edges = self.getInfoFromEdges()
		adj_list: list[tuple[int, int]] = []

		for edge in edges:
			adj_list.append((edge["source_id"], edge["target_id"]))

		return adj_list

	def getDelta(self) -> npt.NDArray[np.string_]:
		nodes = self.getInfoFromNodes()
		edges = self.getInfoFromEdges()

		label_arr = self.getLabelArray()
		adj_matr = self.getAdjMatr()

		# Extract the alphabet as an ordered array.
		sigma = list(set(self.getSigma()))
		sigma.sort()

		# assert sigma != []
		assert sigma

		# Begin delta extraction algorithm.
		delta = np.full((len(nodes), len(sigma)), str)

		# For each source and char in Sigma.
		for src in nodes:
			for char_index, char in enumerate(sigma):
				# First of all, let's check if there are some edges from src to any other nodes.
				src_index = src["node_id"]

				# Id's of the nodes that are reachable from the 'src' node.
				dst_indexes = np.where(adj_matr[src_index] == 1)[0]

				# Time to check if Exists delta(src, char) = dst, for some dst in dst_ids.
				for dst_index in dst_indexes:
					# Extract the (src_index, dst_index) edge to get the upText.
					edge = next(e for e in edges if e["source_id"] == src_index and e["target_id"] == dst_index)

					# Get the allowed transition chars from src_index to dst_index by considering the upText of the edge as a set of chars.
					transition_chars = set(list(edge["upText"]))

					# If the transition is allowed, then set delta as follows:
					if char in transition_chars:
						delta[src_index, char_index] = label_arr[dst_index]

		return delta
