# -*- coding: utf-8 -*-
n = int(input())

for i in range (n):
    um, dois = input().split()
    
    final = ""
    
    tamanhoum = len(um)
    tamanhodois = len(dois)
    
    menor = min(tamanhoum, tamanhodois)
    
    for i in range (menor):
        final += um[i] + dois[i]
        
    final += um[menor:] + dois[menor:]
    
    print(final)
