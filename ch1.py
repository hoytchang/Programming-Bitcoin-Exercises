# Exercise 7
# For p = 7, 11, 17, 31, 43, what is this set in F_p?
# {1**(p-1), 2**(p-1), 3**(p-1), 4**(p-1), ... (p-1)**(p-1)}
plist = [7, 11, 17, 31, 43]
for p in plist:
	set_Fp = []
	for i in range(1,p):
		elem = i**(p-1)
		elem = elem%p
		set_Fp.append(elem)
	print('p = '+str(p))
	print(set_Fp)