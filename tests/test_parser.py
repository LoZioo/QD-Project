from src.parser import Parser

def test_Parser() -> None:
	parser = Parser("docs/Esempio di delta.graphml")

	print("\n\nget_info_from_nodes")
	print(parser.get_info_from_nodes())

	print("\nget_info_from_edges")
	print(parser.get_info_from_edges())

	print("\ngetPositions")
	print(parser.getPositions())

	print("\ngetSigma")
	print(parser.getSigma())
