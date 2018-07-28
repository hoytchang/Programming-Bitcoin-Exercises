# to run this in command prompt: py -3.5 -m unittest test_ecc.py
from ecc import FieldElement, Point
import unittest

class ECCTest(unittest.TestCase):

	def test_on_curve(self):
		prime = 223
		a = FieldElement(0,prime)
		b = FieldElement(7,prime)

		valid_points = ((192,105), (17,56), (1,193))
		invalid_points = ((200,119), (42,99))

		# iterate over valid points
		for x_raw, y_raw in valid_points:
			x = FieldElement(x_raw, prime)
			y = FieldElement(y_raw, prime)
			# Creating the point should not result in an error
			Point(x,y,a,b)

		# iterate over invalid points
		for x_raw, y_raw in invalid_points:
			x = FieldElement(x_raw, prime)
			y = FieldElement(y_raw, prime)
			# check that creating the point results in a ValueError
			with self.assertRaises(ValueError):
				Point(x,y,a,b)

# alternatively, run this in command prompt: py -3.5 test_ecc.py
if __name__ == '__main__':
	unittest.main()