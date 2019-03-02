#chapter 1 exercise 5
prime = 19

print('prime = '+str(prime)+', unsorted')
for k in (1,3,7,13,18):
	print([k*i % prime for i in range(prime)])

print('prime = '+str(prime)+', sorted')
for k in (1,3,7,13,18):
	print(sorted([k*i % prime for i in range(prime)]))

notprime = 20

print('notprime = '+str(notprime)+', unsorted')
for k in (1,3,7,13,18):
	print([k*i % notprime for i in range(notprime)])

print('notprime = '+str(notprime)+', sorted')
for k in (1,3,7,13,18):
	print(sorted([k*i % notprime for i in range(notprime)]))