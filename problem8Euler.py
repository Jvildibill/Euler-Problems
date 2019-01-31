# -*- coding: utf-8 -*-
import math

number = str(input("What is the string that we are looking at?"))
check = 1
list = []

for num in range(0,len(number)-13):
	check = 1
	for x in range(0,13):
		check = int(number[num+x])*check
	list.append(check)

print max(list)