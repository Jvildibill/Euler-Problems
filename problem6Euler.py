# -*- coding: utf-8 -*-
import math

number = input("What number should we check?")
sumSqr = 0
sqrSum = 0

for x in range(1,number+1):
	sumSqr = sumSqr +(x*x)
	sqrSum = sqrSum + x

sqrSum = sqrSum * sqrSum
print sumSqr
print sqrSum
print sqrSum-sumSqr
