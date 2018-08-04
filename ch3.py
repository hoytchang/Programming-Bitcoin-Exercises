from ecc import FieldElement, Point
# Exercise 4
# For the curve y**2 = x**3 + 7 over F_223, find 21*(47,71)
prime = 223
a = FieldElement(0,prime)
b = FieldElement(7,prime)
x = FieldElement(47,prime)
y = FieldElement(71,prime)
p = Point(x,y,a,b)
for s in range(1,21):
	result = s*p
	print('{}*(47,71) = ({},{})'.format(s,result.x.num,result.y.num))