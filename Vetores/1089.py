# -*- coding: utf-8 -*-
while True: 

    n = int(input()) #lê o número de casos de teste 
    
    if n == 0:
        break
    
    h = input().split()
    for i in range (n): #transforma o h em inteiro para o range n
        h [i] = int(h[i])
        
    h.append(h[0])
    h.append(h[1])
    
    p = 0 #armazena os picos
    for i in range (1,n+1):
        if h[i] > h[i-1] and h[i] > h[i+1] or h[i] < h[i-1] and h[i] < h[i+1]:
            p += 1 
            
    print (p)
