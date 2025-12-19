# -*- coding: utf-8 -*-
c = int(input())

for _ in range(c):
    
    m = input().split()
    m [0] = int(m[0])
    
    soma = 0 
    for i in range (1, m[0]+1):
        m [i] = int(m[i])
        soma += m[i]
        
        
    mediaturma = soma / m[0]
    
    qtacimadamedia = 0 
    for i in range (1, m[0]+1):
        if m[i] > mediaturma:
            qtacimadamedia += 1
            
    percacimamedia = qtacimadamedia / m[0] * 100 
    
    print ("%.3f%%" % percacimamedia)
        
