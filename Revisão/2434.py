# -*- coding: utf-8 -*-
a, b = map(int,input().split())

lista = []
saldo = b

for i in range (a):
    valor = int(input())
    
    saldo += valor
    lista.append(saldo)
        
print (min(lista))
