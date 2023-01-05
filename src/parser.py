# xml.etree.ElementTree module implements an API for parsing and creating XML data.
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

class Parser:
	# XML tree root.
	root: Element

	# Constructor.
	def __init__(self, pathname: str) -> None:
		assert pathname[len(pathname)-8 : len(pathname)] == ".graphml"

		mytree = ET.parse(pathname)
		self.root = mytree.getroot()

	def get_info_from_nodes(self):
		nodes = []

		for item in self.root.findall(".//graph/node"):
			# Dictionary.
			node = {
				"posX":			item.attrib["positionX"],
				"posY":			item.attrib["positionY"],
				"node_id":	item.attrib["id"],
				"label":		item.attrib["mainText"]
			}
			nodes.append(node)

		# So I have an array of dictionaries.
		return nodes

	def get_info_from_edges(self):
		edges = []

		for item in self.root.findall(".//graph/edge"):
			# Dictionary.
			edge = {
				"source":	item.attrib["source"],
				"target":	item.attrib["target"],
				"upText":	item.attrib["upText"]
			}
			edges.append(edge)

		# So I have an array of dictionaries.
		return edges

	def getPositions(self):
		positions = []
		nodes = self.get_info_from_nodes()

		for node in nodes:
			positions.append((int(float(node["posX"])), int(float(node["posY"]))))

		# Array of x,y couples.
		return positions
