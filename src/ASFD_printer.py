import networkx as nx
import matplotlib.pyplot as plt
from src.parser import Parser
from src.DirectGraphPrinter import DirectGraphPrinter



class ASFDPrinter(DirectGraphPrinter):

	edge_label : dict[tuple[str,str], str]
	final_state: set[str]

	#Call the constructor of the class DirectGraphPrinter and inizialize edge_label and final_state
	def __init__(self, p: Parser) -> None :
		super().__init__(p)

		self.edge_label = self.getEdgeLabels(p)

		self.final_state = p.getFinalStates()

	#Extract the labels of the edges
	def getEdgeLabels(self, p:Parser) -> dict[tuple[str,str], str] :
		edges = p.getInfoFromEdges()
		label_arr = p.getLabelArray()

		d = {}
		for edge in edges:
			d[( label_arr[edge["source_id"]], label_arr[edge["target_id"]])] = edge["upText"]

		return d

	#Print an image of the ASFD using the functions of the library Network.x
	#By passing a path through the parameter "path" the image will be saved in the desired location
	def printASFD(self, path: str ="") -> None :

		plt.figure(figsize=(15,10))
		nx.draw_networkx(
			self.graph_to_print, self.positions, width=2, linewidths=2,
			node_size=500, node_color='white', font_size = 10, alpha = 0.7, edgecolors = 'black',
			labels={node: node for node in self.graph_to_print.nodes()}
		)

		#The final_node is printed in orange
		nx.draw_networkx_nodes(self.graph_to_print,self.positions, node_size=500, nodelist=self.final_state, node_color="tab:orange", alpha=0.2, edgecolors = 'black')

		#shifting positions for a better visualisation of edge labels
		edge_labels_pos : dict[str, tuple[int, int]] ={}
		for pos in self.positions:
			edge_labels_pos[pos] = (self.positions[pos][0], self.positions[pos][1] + 8)


		nx.draw_networkx_edge_labels(
			self.graph_to_print, edge_labels_pos,
			edge_labels= self.edge_label, label_pos=0.5, font_size= 12,
			font_color='blue', alpha=0.8,
		)
		plt.axis('off')

		if path != "":
			plt.savefig(path)
		plt.show()
