# -*- coding: utf-8 -*-
import math

number = long(input("What’s the number?"))

list = []
count = 0
count1 = 0

for a in range(2,long(math.sqrt(number))+1):
	if number%a==0:
		count=0
		count1=0
		for x in range(2,long(math.sqrt(a)+1)):
			if a%x==0:
				count=1
		if count==0:
			list.append(a)
		for x in range(2,long(math.sqrt((number/a))+1)):
			if (number/a)%x==0:
				count1=1
		if count1==0:
			list.append(number/a)

# commented this out to see the prime factorization
# print list
if len(list)>0:
	print max(list)
else:
	print "Prime!"