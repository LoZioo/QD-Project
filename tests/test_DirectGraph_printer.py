from src.DirectGraph_printer import DirectGraphPrinter
from src.parser import Parser

import numpy as np
import cv2

def test_DirectGraphPrinter() -> None:
	parser = Parser("docs/Esempio di delta.graphml")
	printer = DirectGraphPrinter(parser)

	# getLabeledAdjList.
	expected_adj_list = [("q1", "q2"), ("q2", "q3"), ("q3", "q4"), ("q1", "q4"), ("q4", "q4"), ("q2", "q2"), ("q3", "q3")]
	assert expected_adj_list == printer.getLabeledAdjList()

	# getNodePositions.
	expected_positions = {"q1": (321, 147), "q2": (464, 63), "q3": (605, 139), "q4": (465, 220)}
	assert expected_positions == printer.getNodePositions()

	# save.
	IMG_PATH = "img/saved/graph.jpg"

	# Save the generated image.
	printer.saveGraph(IMG_PATH)

	# MSE comparison.
	saved_image = cv2.imread(IMG_PATH)
	expected_image = cv2.imread("img/tests/DirectGraph_printer_test_graph.jpg")

	saved_image = cv2.cvtColor(saved_image, cv2.COLOR_BGR2GRAY)
	expected_image = cv2.cvtColor(expected_image, cv2.COLOR_BGR2GRAY)

	# MSE calculation.
	h, w = expected_image.shape
	diff = cv2.subtract(expected_image, saved_image)
	err = np.sum(diff**2)
	mse = float(err) / float(h*w)

	assert mse == 0
