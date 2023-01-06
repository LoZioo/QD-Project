import xml.etree.ElementTree as ET					# xml.etree.ElementTree module implements an API for parsing and creating XML data.
from xml.etree.ElementTree import Element

from typing import TypedDict

class Node_t(TypedDict):
	posX:			int
	posY:			int
	node_id:	int
	label:		str

class Edge_t(TypedDict):
	source_id:	int
	target_id:	int
	upText:			str

class Parser:
	# XML tree root.
	root: Element

	# Constructor.
	def __init__(self, pathname: str) -> None:
		assert pathname[len(pathname)-8 : len(pathname)] == ".graphml"

		mytree = ET.parse(pathname)
		self.root = mytree.getroot()

	def get_info_from_nodes(self) -> list[Node_t]:
		nodes: list[Node_t] = []

		for item in self.root.findall(".//graph/node"):
			node: Node_t = {
				"posX":			int(float(item.attrib["positionX"])),
				"posY":			int(float(item.attrib["positionY"])),
				"node_id":	int(item.attrib["id"]),
				"label":		item.attrib["mainText"]
			}
			nodes.append(node)

		# So I have an array of dictionaries.
		return nodes

	def get_info_from_edges(self) -> list[Edge_t]:
		edges: list[Edge_t] = []

		for item in self.root.findall(".//graph/edge"):
			edge: Edge_t = {
				"source_id":	int(item.attrib["source"]),
				"target_id":	int(item.attrib["target"]),
				"upText":			item.attrib["upText"]
			}
			edges.append(edge)

		# So I have an array of dictionaries.
		return edges

	def getPositions(self) -> list[tuple[int, int]]:
		positions: list[tuple[int, int]] = []
		nodes = self.get_info_from_nodes()

		for node in nodes:
			coord = (node["posX"], node["posY"])
			positions.append(coord)

		# Array of x,y couples.
		return positions

	def getSigma(self) -> str:
		sigma: str
		sigma = ''
		
		for	item in self.root.findall(".//graph./edge"):
			sigma = sigma + item.attrib['upText']
	  
		#Sigma string with all of the values from upText of edges	 
		return sigma

	def getEntryState(self) -> str:
		entryState: str
		string: str
		entryState = ''
		string = ''

		for item in self.root.findall(".//graph/node"):
			string = item.attrib["mainText"]
			if string[0] == "_":
				entryState = string
				
		assert entryState[0] == "_"
		return entryState

