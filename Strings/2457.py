# -*- coding: utf-8 -*-
letra = input().strip()
frase = input().split()

palavrassim = 0
palavrastotal = 0

for palavra in frase:
    palavrastotal += 1
    
    if letra in palavra:
        palavrassim += 1

porcentagem = (palavrassim / palavrastotal) * 100

print ("%.1f" % porcentagem)

