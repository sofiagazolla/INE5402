# -*- coding: utf-8 -*-
leituras, maxima = list(map(int,input().split()))

ultrapassou = 0 

elevador = 0 
for i in range (leituras):
    sairam, entraram = list(map(int,input().split()))
    
    elevador += entraram
    elevador -= sairam
    
    if elevador > maxima:
        ultrapassou += 1 
        
    else: 
        ultrapassou += 0 
        
if ultrapassou > 0:
    print("S")
    
else:
    print("N")
