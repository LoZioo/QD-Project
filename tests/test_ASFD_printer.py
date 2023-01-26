from src.ASFD_printer import ASFDPrinter
from src.parser import Parser

import numpy as np
import cv2

def test_ASFDPrinter() -> None:
	parser = Parser("docs/Esempio di delta.graphml")
	printer = ASFDPrinter(parser)

	# getEdgeTransitions.
	expected_transitions = {("q1", "q2"): "a", ("q2", "q3"): "b", ("q3", "q4"): "a", ("q1", "q4"): "b", ("q4", "q4"): "ab", ("q2", "q2"): "a", ("q3", "q3"): "b"}
	assert expected_transitions == printer.getEdgeTransitions()

	# saveASFD.
	IMG_PATH = "img/saved/ASFD.jpg"

	# Save the generated image.
	printer.saveASFD(IMG_PATH)

	# MSE comparison.
	saved_image = cv2.imread(IMG_PATH)
	expected_image = cv2.imread("img/tests/ASFD_printer_test_graph.jpg")

	saved_image = cv2.cvtColor(saved_image, cv2.COLOR_BGR2GRAY)
	expected_image = cv2.cvtColor(expected_image, cv2.COLOR_BGR2GRAY)

	# MSE calculation.
	h, w = expected_image.shape
	diff = cv2.subtract(expected_image, saved_image)
	err = np.sum(diff**2)
	mse = float(err) / float(h*w)

	assert mse == 0
