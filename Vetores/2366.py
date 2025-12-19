# -*- coding: utf-8 -*-
n, m = input().split()
n = int(n)
m = int(m)
p = list(map(int,input().split()))

consegue = True

for i in range (1, n):
    distancia = p[i] - p[i-1]
    
    if distancia > m:
        consegue = False
        
    if consegue and 42195 - p[n-1] > m:
        consegue = False

if consegue == True:
    print ("S")
    
else:
    print ("N")
