# -*- coding: utf-8 -*-
while True:
    n = int(input())
    
    if n == 0:
        break
    t = 0 
    
    for x in range (1, n+1):
        t += (n - x + 1) ** 2
    
    print("%d" % (t))
