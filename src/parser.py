import xml.etree.ElementTree as ET
# xml.etree.ElementTree module implements an API for parsing and creating XML data
from xml.etree.ElementTree import Element

class Parser:
	root: Element
	# Constructor
	def __init__(self, pathname: str):
		assert pathname[len(pathname)-8:len(pathname)] == '.graphml'
		mytree = ET.parse(pathname)
		self.root = mytree.getroot()

	def get_info_from_nodes(self):
		nodes = []
		for item in self.root.findall('.//graph/node'):
			# Dictionaries
			node = {
				'posX' : item.attrib['positionX'],
				'posY' : item.attrib['positionY'],
				'node_id' : item.attrib['id'],
				'label' : item.attrib['mainText']
			}
			nodes.append(node)
			# So I have an array of dictionaries
		return nodes

	def get_info_from_edges(self):
		edges = []
		for item in self.root.findall('.//graph/edge'):
			# Dictionaries
			edge = {
				'source' : item.attrib['source'],
				'target' : item.attrib['target'],
				'upText' : item.attrib['upText']
			}
			edges.append(edge)
			# So I have an array of dictionaries
		return edges
