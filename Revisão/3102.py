# -*- coding: utf-8 -*-
n = int(input())

for i in range (n):
    x1, y1, x2, y2, x3, y3 = list(map(float,input().split()))
    
    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    
    print ("%.3f" % area)

