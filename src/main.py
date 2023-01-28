from src.parser import Parser
from src.graph import DirectGraph_init_t
from src.ASFD import ASFD, ASFD_init_t
from src.ASFD_printer import ASFDPrinter

def main() -> None:
	ASFD_TO_PARSE = "docs/Esempio main 1.graphml"
	GRAPH_IMG_TO_SAVE = "img/saved/main_graph.jpg"
	ASFD_IMG_TO_SAVE = "img/saved/main_ASFD.jpg"

	parser = Parser(ASFD_TO_PARSE)
	printer = ASFDPrinter(parser)

	GRAPH_INIT = DirectGraph_init_t(
		adj_matr = parser.getAdjMatr(),
		label_arr = parser.getLabelArray()
	)

	ASFD_INIT = ASFD_init_t(
		sigma = parser.getSigma(),
		delta = parser.getDelta(),
		entry_state = parser.getEntryState(),
		final_states = parser.getFinalStates(),
	)

	asfd = ASFD(ASFD_INIT, GRAPH_INIT)
	print("m = (Q, Sigma, delta, q0, F)")
	print("Where m is relative to the file \"%s\"." % ASFD_TO_PARSE)
	print()

	print("Q: %s" % parser.getLabelArray())
	print("Sigma: %s" % parser.getSigmaNormalized())
	print("delta:")
	print(parser.getDelta())
	print()

	print("q0: %s" % parser.getEntryState())
	print("F: %s" % parser.getFinalStates())
	print()

	print("String testing:")
	strings = ("000010", "0000101")

	for x in strings:
		print("  %s: %s" % (x, str(asfd.evaluate(x))))
	print()

	print("Saving graph to \"%s\"..." % GRAPH_IMG_TO_SAVE)
	print("Saving ASFD to \"%s\"..." % ASFD_IMG_TO_SAVE)

	printer.saveGraph(GRAPH_IMG_TO_SAVE)
	printer.saveASFD(ASFD_IMG_TO_SAVE)
