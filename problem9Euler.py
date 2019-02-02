# -*- coding: utf-8 -*-
import math

list = []
a = 0 
b = 0
c = 0

for n in range (1,50):
	for m in range (2,50):
		if m>n:
			a = m**2 - n**2
			b = m*n*2
			c = m**2 + n**2
			for x in range (1,50):
				if a*x + b*x + c*x ==1000:
					print a*x
					print b*x
					print c*x
					print a*b*c*x*x*x