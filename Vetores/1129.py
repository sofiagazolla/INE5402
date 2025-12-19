# -*- coding: utf-8 -*-
while True:
    n = int(input())
    if n == 0:
        break
        
    for _ in range (0,n):
        l = input().split()
        resposta = 0 
        marcada = 0 
        
        for i in range (0,len(l)):
            l[i] = int(l[i])
            
            if l[i] <= 127:
                resposta += 1 
                marcada = i 
                
        if resposta == 1:
            if marcada == 0:
                print ("A")
                
            elif marcada == 1:
                print ("B")
                
            elif marcada == 2:
                print ("C")
                
            elif marcada == 3:
                print ("D")
                
            else:
                print ("E")
                
        else:
            print ("*")
