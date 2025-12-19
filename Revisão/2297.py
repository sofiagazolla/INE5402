# -*- coding: utf-8 -*-
teste = 0 

while True:
    cartas = int(input())
    
    if cartas == 0:
        break
    
    aldo = 0 
    beto = 0 
    
    teste += 1 
    
    print ("Teste %d" % teste)
    
    for i in range (cartas):
        a, b = map(int,input().split())
        
        aldo += a 
        beto += b 
    
    if aldo > beto:
        print ("Aldo")
        print ()
        
    else:
        print ("Beto")
        print ()
