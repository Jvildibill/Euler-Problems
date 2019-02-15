# -*- coding: utf-8 -*-
import math

list  = []
list1 = []
list2 = []
product = 0

f = open("EulerProblem11.txt", "r")
list = f.read().split()

		
for x in range (0,339,20):
	for y in range (0,19):
		z = x+y
		if x<340:
			list1.append(int(list[z])*int(list[z+20])*int(list[z+40])*int(list[z+60]))
		if y<17 and x<340:
			list1.append(int(list[z])*int(list[z+21])*int(list[z+42])*int(list[z+63]))
		if y>2 and x<340:
			list1.append(int(list[z])*int(list[z+19])*int(list[z+38])*int(list[z+57]))
		if y<17:
			list1.append(int(list[z])*int(list[z+1])*int(list[z+2])*int(list[z+3]))
print max(list1)