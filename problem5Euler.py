# -*- coding: utf-8 -*-
import math

highend = input("What should the high end be?")
y=0
count = 0

for x in range(1,highend):
	y = 20*x
	if (y%19==0 and y%18==0 and y%17==0 and y%16==0 and y%15==0 and y%14==0 and y%13==0 and y%12==0 and y%11==0):
		print(y)
		count = 1
		break
if count==0:
	print("Nope")