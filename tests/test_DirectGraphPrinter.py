import numpy as np
from src.parser import Parser
from src.DirectGraphPrinter import DirectGraphPrinter

def test_DirectGraphPrinter() -> None:
    parser = Parser("docs/Esempio di delta.graphml")
    printerDG = DirectGraphPrinter(parser)

    #test toCouple
    couple_list : list[(str,str)] = [('q1', 'q2'), ('q1', 'q4'), ('q2', 'q2'), ('q2', 'q3'), ('q3', 'q3'), ('q3', 'q4'), ('q4', 'q4')]
    extracted_list: list[(str,str)] = printerDG.toCouple(parser)

    np.testing.assert_equal(couple_list,extracted_list)

    #test getPositions
    position_dict : dict[str, tuple[int,int]] = {'q1': (321, 147), 'q2': (464, 63), 'q3': (605, 139), 'q4': (465, 220)}
    extracted_dict : dict[str, tuple[int,int]] = printerDG.getPositions(parser)
    
    np.testing.assert_equal(position_dict, extracted_dict)