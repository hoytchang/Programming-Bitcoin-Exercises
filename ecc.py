import math

class FieldElement:
	
	def __init__(self, num, prime):
		if num < 0 or num >= prime:
			raise ValueError('num should be between 0 and {}-1'.format(prime))
		self.num = num
		self.prime = prime
	
	def __eq__(self, other):
		if isinstance(other,FieldElement):
			return self.num == other.num and self.prime == other.prime
		else:
			return False
	
	def __ne__(self, other):
		return self.num != other.num or self.prime != other.prime

	def __repr__(self):
		return 'FieldElement_{}({})'.format(self.prime, self.num)

	def __add__(self,other):
		if self.prime != other.prime:
			raise RuntimeError('cannot add two numbers in different Fields')
		num = (self.num + other.num) % self.prime
		return self.__class__(num, self.prime)

	def __sub__(self,other):
		if self.prime != other.prime:
			raise RuntimeError('cannot subtract two numbers in different Fields')
		num = (self.num - other.num) % self.prime
		return self.__class__(num, self.prime)

	def __mul__(self,other):
		if self.prime != other.prime:
			raise RuntimeError('cannot multiply two numbers in different Fields')
		num = (self.num * other.num) % self.prime
		return self.__class__(num, self.prime)

	def __pow__(self, exponent):
		n = exponent % (self.prime - 1)
		num = pow(self.num, n, self.prime)
		return self.__class__(num, self.prime)

	def __truediv__(self,other):
		if self.prime != other.prime:
			raise RuntimeError('cannot divide two numbers in different Fields')
		# use the formula a/b = ab**-1 = ab**(p-2)
		num1 = pow(other.num, other.prime-2, other.prime)
		num1_FE = self.__class__(num1, self.prime)
		num2_FE = self * num1_FE
		return num2_FE

	def __rmul__(self, coefficient):
		c = FieldElement(coefficient,self.prime)
		return self * c

class Point:

	zero = 0

	def __init__(self, x, y, a, b):
		self.a = a
		self.b = b
		self.x = x
		self.y = y
		
		# special case
		if self.x is None and self.y is None:
			return

		# check that point is on curve
		LHS = self.y**2
		RHS = self.x**3 + self.a * self.x + self.b
		if isinstance(LHS,FieldElement): #convert from FieldElement to float for math.isclose()
			LHS = LHS.num
			RHS = RHS.num
		if not math.isclose(LHS, RHS):
			raise ValueError('Point ({},{}) is not on the curve where a,b={},{}'.format(x,y,a,b))

	def __eq__(self, other):
		return self.a == other.a and self.b == other.b and self.x == other.x and self.y == other.y

	def __ne__(self, other):
		return self.a != other.a or self.b != other.b or self.x != other.x or self.y != other.y

	def __repr__(self):
		return 'Point ({},{}) on curve a,b={},{}'.format(self.x, self.y, self.a, self.b)

	def __add__(self, other):
		if self.x is None:
			return other
		if other.x is None:
			return self
		if self.x != other.x:
			s = (other.y - self.y)/(other.x - self.x)
			x = s**2 - self.x - other.x
			y = s*(self.x - x) - self.y
			return self.__class__(x, y, self.a, self.b)
		if self == other and self.y == self.zero:
			return self.__class__(None, None, self.a, self.b)
		if self.x == other.x and self.y == other.y:
			s = (3*self.x**2 + self.a)/(2*self.y)
			x = s**2 - 2*self.x
			y = s*(self.x - x) - self.y
			return self.__class__(x, y, self.a, self.b)
		if self.x == other.x:
			return self.__class__(None, None, self.a, self.b)

	def __rmul__(self, coefficient):
		product = self.__class__(None,None,self.a,self.b)
		for _ in range(coefficient):
			product += self
		return product
