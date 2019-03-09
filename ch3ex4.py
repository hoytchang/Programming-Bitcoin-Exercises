from ecc import FieldElement, Point
# Exercise 4
# For the curve y**2 = x**3 + 7 over F_223, find 2*(192,105)
prime = 223
a = FieldElement(0,prime)
b = FieldElement(7,prime)
x = FieldElement(192,prime)
y = FieldElement(105,prime)
p = Point(x,y,a,b)
print('2 * (192,105) = ' + str(2*p))

# For the curve y**2 = x**3 + 7 over F_223, find 21*(47,71)
x = FieldElement(47,prime)
y = FieldElement(71,prime)
p = Point(x,y,a,b)
for s in range(1,22):
	result = s*p
	#print('{}*(47,71) = ({},{})'.format(s,result.x.num,result.y.num))
	print('{}*(47,71) = '.format(s), result)
	