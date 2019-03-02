# chapter 1 exercise 8
# solve the following in Field 31
# 3 / 24
# 17 ^ -3
# 4 ^ -4 * 11
print("3 / 24 = ")
print((3 * 24 **(31-2)) % 31)

#solving, using the faster way
print("3 / 24 = ")
print(3*pow(24,31-2,31) % 31)
print("17 ^ -3 = ")
print(pow(17,31-4,31))
print("4 ^ -4 * 11 = ")
print(pow(4,31-5,31)*11%31)

#solve the same problems, using ecc.py
from ecc import FieldElement

print("3 / 24 = ")
a = FieldElement(3,31)
b = FieldElement(24,31)
print(a/b)
print("17 ^ -3 = ")
b = FieldElement(17,31)
print(pow(b,-3))
print(b**(-3))