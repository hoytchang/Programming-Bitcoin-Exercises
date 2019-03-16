# chapter 3 example 9 verify a signature
from ecc import S256Point, G, N

# z, the hash of the thing signed
z = 0xbc62d4b80d9e36da29c16c5d4d9f11731f36052c72401a76c23c0fb5a9b74423

# (r,s), the signature
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec

# P, the public key
px = 0x04519fac3d910ca7e7138f7013706f619fa8f033e6ec6e09370ea38cee6a7574
py = 0x82b51eab8c27c66e26c858a079bcdf4f1ada34cec420cafc7eac1a42216fb6c4
point = S256Point(px,py)

# compute s**-1
s_inv = pow(s, N-2, N) #using fermat's little theorem, since N is prime

# compute u = z / s
u = z * s_inv % N

# compute v = r / s
v = r * s_inv % N

# compute R = kG = uG + vP
R = u*G + v*point

# compare r with the x-coordinate of R
print(R.x.num == r)