from ecc import FieldElement, Point
# Exercise 4
# For the curve y**2 = x**3 + 7 over F_223, find 21*(47,71)
prime = 223
a = FieldElement(0,prime)
b = FieldElement(7,prime)
x = FieldElement(192,prime)
y = FieldElement(105,prime)
p1 = Point(x,y,a,b)
for n in range(1,22):
	print(n)
	pn = n*p1 #TODO fix unspported operand type for *: int and Point
	print(pn)