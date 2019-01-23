# -*- coding: utf-8 -*-
import math

number = input("Which prime do you want to find?")
number = number -1
count = 1
x = 3
list = []

while count<(number+1):
	isprime = 1
	for a in range(2,int(math.sqrt(x))+1):
		if x%a==0:
			isprime = 0
	if isprime == 1:
		list.append(x)
		count = count +1
	x= x+2


print max(list)
