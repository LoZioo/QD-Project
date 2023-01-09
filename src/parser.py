import numpy as np
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
		nodes = self.get_info_from_nodes()

		for node in nodes:
			string = (node["label"])
			if string[0] == "_":
				entryState = string[1:len(string)]

		assert entryState != ''
		return entryState

	def getFinalStates(self) -> list[str]:
		finalStates: list[str] = []
		state: str
		state = ''
		nodes = self.get_info_from_nodes()

		for node in nodes:
			state = (node["label"])
			if state[len(state)-1] == "_":
				state = state[0:len(state)-1]
				finalStates.append(state)

		assert finalStates != []
		return finalStates

	def getLabelArray(self) -> list[str]:
		labelArray: list[str] = []
		state: str
		state = ''
		nodes = self.get_info_from_nodes()

		for node in nodes:
			state = (node["label"])
			if state[0] == "_":
				state = state[1:len(state)]
			if state[len(state)-1] == "_":
				state = state[0:len(state)-1]
			labelArray.append(state)
    
		return labelArray

	def get_adj_Matrix(self) -> list[list[int]]:
		state_count : int
		state_count = 0

		for item in self.root.findall('.//graph/node'):
			state_count += 1 #Get the dim of the adj_matrix

		adj_Matrix = np.zeros((state_count,state_count))  #created adj_matrix full of zeros

		dictionary = self.get_info_from_edges()
		for x in dictionary:
			adj_Matrix[x["source_id"]][x["target_id"]] = 1

		return adj_Matrix	

	def get_delta_Matrix(self) -> list[list[str]]:
		distinct_states = self.getLabelArray()
		distinct_deltas = []
		nodes = self.get_info_from_nodes()
		edges = self.get_info_from_edges()
		for edge in edges:
			delta = (edge['upText'])
			for i in delta:
				if i not in distinct_deltas:
					distinct_deltas.append(i)
		distinct_deltas.sort()
		assert distinct_deltas != []

		delta_Matrix = [["" for x in range(len(distinct_deltas))] for y in range (len(distinct_states))]

		count_delta_pos = -1
		count_pos_substr = -1
		temp = 0
		for i in range(0,len(distinct_states)): 
			for item in edges:               
				if item["source_id"] == i: 
					if len(item["upText"]) < 2: # if the upText is with only 1 char
						for j in range(0,len(distinct_deltas)):     
							for char in distinct_deltas: 
								count_delta_pos += 1 
								if item["upText"] == char: 
									temp = count_delta_pos #save the value of the correct collumn
									count_delta_pos = -1 #have to reset the position once we found the correct upText
									break
							for x in range(0,len(nodes)): 
								if item["target_id"] == nodes[x]["node_id"]: 
									delta_Matrix[i][temp] = distinct_states[item["target_id"]] 
									break
					else: #for all uptext with more then 1 char
						for v in range(0,len(item["upText"])):
							for j in range(0,len(distinct_deltas)):     
								for char in distinct_deltas: 
									count_delta_pos += 1 
									count_pos_substr += 1
									if item["upText"][count_pos_substr:count_pos_substr+1] == char: 
										temp = count_delta_pos 
										for x in range(0,len(nodes)): 
											if item["target_id"] == nodes[x]["node_id"]: 
												delta_Matrix[i][temp] = distinct_states[item["target_id"]] 
												break
								count_delta_pos = -1 #we reset it here because now we are dealing with strings and not chars   
		return delta_Matrix
