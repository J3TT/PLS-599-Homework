#!bin/user/python
a = 4549
b = 9178
sum = 0

for n in range(a, b):
	if n % 2 == 1:
		sum = sum + n
		
print (sum)