from src.parser import Parser

def test_Parser() ->None:
  parser = Parser("docs/Esempio di delta.graphml")
  print (parser.get_info_from_nodes())