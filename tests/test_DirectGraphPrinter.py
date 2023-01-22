import numpy as np
from src.parser import Parser
from src.DirectGraphPrinter import DirectGraphPrinter

def test_DirectGraphPrinter() -> None:
    parser = Parser("docs/Esempio di delta.graphml")
    printerDG = DirectGraphPrinter(parser)

    #test toCouple
    couple_list : list[(str,str)] = [('q1', 'q2'), ('q1', 'q4'), ('q2', 'q2'), ('q2', 'q3'), ('q3', 'q3'), ('q3', 'q4'), ('q4', 'q4')]
    extracted_list: list[(str,str)] = printerDG.toCouple(parser)

    assert np.array_equal(couple_list,extracted_list)