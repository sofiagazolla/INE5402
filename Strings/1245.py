# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())
        
        pares = 0
        dicionario = {}
        
        for i in range (n):
            numero, pe = input().split()
            
            if numero in dicionario:
                dicionario[numero].append(pe)
            else:
                dicionario[numero] = [pe]
        
        for numero in dicionario:
            esquerdo = dicionario[numero].count('E')
            direito = dicionario[numero].count('D')
            pares += min(esquerdo,direito)
        
        print (pares)
        
    except EOFError:
        break
