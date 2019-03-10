# to run this in command prompt: py -3.5 -m unittest test_ecc.py
from ecc import FieldElement, Point, S256Point, G, N, Signature, PrivateKey
import unittest
from random import randint

class ECCTest(unittest.TestCase):

	def test_add_FE(self):
		a = FieldElement(5,7)
		b = FieldElement(4,7)
		c = FieldElement(2,11)
		self.assertEqual(a+b,FieldElement(2,7))
		with self.assertRaises(RuntimeError):
			b+c

	def test_pow_FE(self):
		a = FieldElement(17,31)
		b = -3
		c = pow(a,b)
		d = FieldElement(29,31)
		self.assertEqual(c,d)

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
	
	def test_Point_scalar_multiply(self):
		prime = 223
		a = FieldElement(0,prime)
		b = FieldElement(7,prime)
		x = FieldElement(47,prime)
		y = FieldElement(71,prime)
		p = Point(x,y,a,b)

		x6 = FieldElement(139,prime)
		y6 = FieldElement(137,prime)
		p6 = Point(x6,y6,a,b)
		result = 6*p
		self.assertEqual(result,p6)

		result = 21*p
		self.assertEqual(result.x,None)
		self.assertEqual(result.y,None)

	def test_nG_on_secp256k1(self):
		inf = S256Point(None, None)
		self.assertEqual(N*G, inf)

	def test_pubpoint(self):
		points = (
			# secret, x, y
			(7, 0x5cbdf0646e5db4eaa398f365f2ea7a0e3d419b7e0330e39ce92bddedcac4f9bc, 0x6aebca40ba255960a3178d6d861a54dba813d0b813fde7b5a5082628087264da),
			(1485, 0xc982196a7466fbbbb0e27a940b6af926c1a74d5ad07128c82824a11b5398afda, 0x7a91f9eae64438afb9ce6448a1c133db2d8fb9254e4546b6f001637d50901f55),
			(2**128, 0x8f68b9d2f63b5f339239c1ad981f162ee88c5678723ea3351b7b444c9ec4c0da, 0x662a9f2dba063986de1d90c2b6be215dbbea2cfe95510bfdf23cbf79501fff82),
			(2**240 + 2**31, 0x9577ff57c8234558f293df502ca4f09cbc65a6572c842b39b366f21717945116, 0x10b49c67fa9365ad7b90dab070be339a1daf9052373ec30ffae4f72d5e66d053),
		)
		for secret, x, y in points:
			# initialize the secp256k1 point
			point = S256Point(x,y)
			# check that te secret*G is the same as the point
			self.assertEqual(secret*G, point)

	def test_verify(self):
		point = S256Point(
			0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c,
			0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34)
		z = 0xec208baa0fc1c19f708a9ca96fdeff3ac3f230bb4a7ba4aede4942ad003c0f60
		r = 0xac8d1c87e51d0d441be8b3dd5b05c8795b48875dffe00b7ffcfac23010d3a395
		s = 0x68342ceff8935ededd102dd876ffd6ba72d6a427a3edb13d26eb0781cb423c4
		self.assertTrue(point.verify(z, Signature(r, s)))
		z = 0x7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
		r = 0xeff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c
		s = 0xc7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6
		self.assertTrue(point.verify(z, Signature(r, s)))

	def test_sign(self):
		pk = PrivateKey(randint(0,N))
		z = randint(0, 2**256)
		sig = pk.sign(z)
		self.assertTrue(pk.point.verify(z,sig))


# alternatively, run this in command prompt: py -3.5 test_ecc.py
if __name__ == '__main__':
	unittest.main()