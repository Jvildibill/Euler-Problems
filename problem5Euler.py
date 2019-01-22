# -*- coding: utf-8 -*-
import math

y=0
x=0
count = 0

while count == 0:
	x = x+1
	y = 20*x
	if (y%19==0 and y%18==0 and y%17==0 and y%16==0 and y%15==0 and y%14==0 and y%13==0 and y%12==0 and y%11==0):
		print(y)
		count = 1
