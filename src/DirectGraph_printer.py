# type: ignore
import networkx as nx
import matplotlib.pyplot as plt
from src.parser import Parser

class DirectGraphPrinter:

	graph_to_print: nx.DiGraph	#Graph that this class will print
	positions: dict[str, tuple[int, int]]	#The positions where each node will be printed

	#Inizialize graph_to_print and positions
	def __init__(self, p: Parser) -> None:

		l_adj = self.toCouple(p)
		self.graph_to_print = nx.DiGraph()
		self.graph_to_print.add_nodes_from(p.getLabelArray())
		self.graph_to_print.add_edges_from(l_adj)
		self.positions = self.getPositions(p)

	#Using the adjacency matrix to generate the edges of the couples
	def toCouple(self, p:Parser) -> list[(str,str)]:
		adj_matr = p.getAdjMatr()
		label_arr = p.getLabelArray()
		l = []
		for i in range(len(adj_matr)):
			for j in range(len(adj_matr[i])):
				if adj_matr[i][j] == 1 :
					l = l + [(label_arr[i],label_arr[j])]
		return l

	#Extract the positions of the nodes
	def getPositions(self, p:Parser) -> dict[str, tuple[int, int]] :

		d = {}
		nodes = p.getInfoFromNodes()

		for node in nodes:
			l = node["label"]

			if l[0] == "_":
				l = l[1 : len(l)]

			if l[len(l)-1] == "_":
				l = l[0 : len(l)-1]

			d[l] = (node["posX"], node["posY"])

		return d

	#Print an image of the graph using the functions of the library Network.x
	#By passing a path through the parameter "path" the image will be saved in the desired location
	def printGraph(self, path: str = "") -> None:

		plt.figure(figsize=(15,10))
		nx.draw_networkx(self.graph_to_print, self.positions,node_size= 1000,font_size = 18, node_color= 'white', edgecolors= 'black', linewidths= 2, width= 2)

		ax = plt.gca()
		ax.margins(0.20)
		plt.axis("off")

		if path != "":
			plt.savefig(path)

		plt.show()
