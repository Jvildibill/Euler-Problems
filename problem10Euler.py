# -*- coding: utf-8 -*-
import math

sum = 2
isprime = 0
number = 2000000

for x in range (3,number,2):
	isprime = 1
	while isprime==1:
		for y in range (2,int(math.sqrt(x))+1):
			if x%y ==0:
				isprime = 0
		if isprime==1:
			sum = sum + x
			isprime = 0
print sum