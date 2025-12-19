# -*- coding: utf-8 -*-
teste = 0 

while True:
    
    cinquenta = 0 
    dez = 0
    cinco = 0 
    um = 0 
    
    i = int(input())
    
    if i == 0:
        break
    
    cinquenta += i // 50
    
    dez += (i % 50) // 10
    
    cinco += ((i % 50) % 10) // 5 
    
    um += ((i % 50) % 10) % 5 

    teste += 1 
    
    print ("Teste %d" % teste)
    print ("%d %d %d %d" % (cinquenta, dez, cinco, um))
    print ()

