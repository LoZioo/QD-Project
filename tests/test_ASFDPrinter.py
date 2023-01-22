import numpy as np
from src.parser import Parser
from src.ASFDPrinter import ASFDPrinter

def test_ASFDPrinter() -> None:
    parser = Parser("docs/Esempio di delta.graphml")
    printerASFD = ASFDPrinter(parser)

    #test getEdgeLabels 
    edgeLabels_dict : dict[tuple[str,str],str] = {('q1', 'q2'): 'a', ('q2', 'q3'): 'b', ('q3', 'q4'): 'a', ('q1', 'q4'): 'b', ('q4', 'q4'): 'ab', ('q2', 'q2'): 'a', ('q3', 'q3'): 'b'}
    extracted_dict : dict[tuple[str,str],str] = printerASFD.getEdgeLabels(parser)
    
    np.testing.assert_equal(edgeLabels_dict, extracted_dict)