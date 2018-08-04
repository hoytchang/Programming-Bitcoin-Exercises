# to run this in command prompt: py -3.5 -m unittest test_ecc.py
from ecc import FieldElement, Point
import unittest

class ECCTest(unittest.TestCase):

	def test_add_FE(self):
		a = FieldElement(5,7)
		b = FieldElement(4,7)
		c = FieldElement(2,11)
		self.assertEqual(a+b,FieldElement(2,7))
		with self.assertRaises(RuntimeError):
			b+c

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

	def test_add_Point(self):
		# add a point to another point
		p1 = Point(2,5,5,7)
		p2 = Point(-1,-1,5,7)
		p3 = Point(3,-7,5,7)
		self.assertEqual(p1+p2,p3)

		# add a point to itself
		p4 = Point(-1.1100000000000003,0.2870000000000008,5,7)
		self.assertEqual(p1+p1,p4)

	def test_add_Point_over_FF(self):
		a = FieldElement(0,223)
		b = FieldElement(7,223)
		x1 = FieldElement(192,223)
		y1 = FieldElement(105,223)
		p1 = Point(x1,y1,a,b)

		x2 = FieldElement(17,223)
		y2 = FieldElement(56,223)
		p2 = Point(x2,y2,a,b)

		x3 = FieldElement(170,223)
		y3 = FieldElement(142,223)
		p3 = Point(x3,y3,a,b)
		self.assertEqual(p1+p2,p3)

		x4 = FieldElement(60,223)
		y4 = FieldElement(139,223)
		p4 = Point(x4,y4,a,b)

		x5 = FieldElement(220,223)
		y5 = FieldElement(181,223)
		p5 = Point(x5,y5,a,b)
		self.assertEqual(p3+p4,p5)

		x6 = FieldElement(49,223)
		y6 = FieldElement(71,223)
		p6 = Point(x6,y6,a,b)
		self.assertEqual(p1+p1,p6)
	

# alternatively, run this in command prompt: py -3.5 test_ecc.py
if __name__ == '__main__':
	unittest.main()