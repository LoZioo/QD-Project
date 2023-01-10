from src.parser import Parser

def test_Parser() -> None:
	parser = Parser("docs/Esempio di delta.graphml")

	print("\n\ngetInfoFromNodes:")
	for node in parser.getInfoFromNodes():
		print(node)

	print("\ngetInfoFromEdges:")
	for edge in parser.getInfoFromEdges():
		print(edge)

	print("\ngetPositions:")
	for couple in parser.getPositions():
		print(couple)

	print()
	print("getSigma: %s" % parser.getSigma())
	print("getEntryState: %s" % parser.getEntryState())
	print("getFinalStates: %s" % parser.getFinalStates())
	print("getLabelArray: %s" % parser.getLabelArray())

	print("\ngetAdjMatr")
	print(parser.getAdjMatr())
	
	print("\ngetDelta")
	print(parser.getDelta())
