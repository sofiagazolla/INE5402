# -*- coding: utf-8 -*-
y = input().strip()
mensagem = ""
i = 0 

while i < len(y):
    if y[i] == 'p':
        i += 1 
    if i < len(y):
        mensagem += y[i]
    i += 1 
        
print(mensagem)
