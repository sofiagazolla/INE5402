# -*- coding: utf-8 -*-
n = int(input())
x = input (). split ()

for i in range (0 , len (x)):
    x[i ] = int (x[i ])
m = x [0] 
p = 0 
for i in range (1 , len (x)):
    if x[i] < m :
        m = x[i]
        p = i 
        
print ("Menor valor: %d" % m)
print ("Posicao: %d" % (p))
