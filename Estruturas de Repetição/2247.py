# -*- coding: utf-8 -*-
teste = 0 

while True:
    n = int(input())
    
    diferenca = 0  
    teste += 1 
    
    if n == 0:
        break
    
    print ("Teste %d" % teste)
    
    for _ in range (n):
        j, z = list(map(int,input().split()))
        
        diferenca += j - z
        
        print (diferenca)
        
    print ()
