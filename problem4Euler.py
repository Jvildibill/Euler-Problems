# -*- coding: utf-8 -*-
import math

list = []
for x in range(1,999):
	for y in range(1,999):
		check = str(x*y)
		count = 0
		pcount = 0
		a = len(check)

		if a%2==0:
			for z in range(0,a-1):
				count = count + 1
				if check[z] == check[a-z-1]:
					pcount = pcount+1
			if count == pcount:
				list.append(x*y)
		else:
			for z in range(0,a):
				count = count + 1
				if check[z] == check[a-z-1]:
					pcount = pcount+1
			if count == pcount:
				list.append(x*y)
print max(list)