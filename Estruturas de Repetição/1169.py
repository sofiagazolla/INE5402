# -*- coding: utf-8 -*-
n = int(input())

for _ in range (0,n):
    x = int(input())
    for _ in range (0,x):
        y = ((2**x) - 1) // 12000
        
    print ("%d kg" % (y))
