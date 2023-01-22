import numpy as np
import cv2
from src.parser import Parser
from src.ASFDPrinter import ASFDPrinter


def test_ASFDPrinter() -> None:
	parser = Parser("docs/Esempio di delta.graphml")
	printerASFD = ASFDPrinter(parser)

	#test getEdgeLabels 
	edgeLabels_dict : dict[tuple[str,str],str] = {('q1', 'q2'): 'a', ('q2', 'q3'): 'b', ('q3', 'q4'): 'a', ('q1', 'q4'): 'b', ('q4', 'q4'): 'ab', ('q2', 'q2'): 'a', ('q3', 'q3'): 'b'}
	extracted_dict : dict[tuple[str,str],str] = printerASFD.getEdgeLabels(parser)
	
	np.testing.assert_equal(edgeLabels_dict, extracted_dict)

	#test printASFD
	printerASFD.printASFD("docs/extracted_graph.jpg")
	img_ASFD = cv2.imread("docs/test_ASFD.jpg")
	img_extracted = cv2.imread("docs/extracted_graph.jpg")
	
	img_graph = cv2.cvtColor(img_ASFD, cv2.COLOR_BGR2GRAY)
	img_extracted = cv2.cvtColor(img_extracted, cv2.COLOR_BGR2GRAY)

	#MSE calculation
	h, w = img_graph.shape
	diff = cv2.subtract(img_graph,img_extracted)
	err = np.sum(diff**2)
	mse = err/(float(h*w))
	
	np.testing.assert_equal(mse,0)