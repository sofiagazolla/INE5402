# -*- coding: utf-8 -*-
c = int(input())

for _ in range (c):
    palavra = input()
    p = list(palavra)
    
    for i in range (len(palavra)-1, -1,-1):
        
        if p[i].islower():
            p[i] = "".join(p[i])
            print (p[i], end = "")
            
    print()
