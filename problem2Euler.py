# -*- coding: utf-8 -*-
# commenting out the prints I used to validate the code
# just un comment and you can see the broader sequence
# will calculate the sum as long as the fibonacci sequence  number is under 4000000
# only sums if the values are even



limit = 4000000
a = 1
b = 2
x = 0
sum = 2
# print a
# print b

while x<limit and a<limit and b<limit:
	x = a+b
	if x<limit and x%2==0:
		sum = sum+x
	#print x
	a = b + x
	if a<limit and a%2==0:
		sum = sum+a
	# print a
	b = x + a
	if b<limit and b%2==0:
		sum = sum+b
	# print b

print "sum is %d" % sum