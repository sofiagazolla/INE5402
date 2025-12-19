# -*- coding: utf-8 -*-
n, m = map(int,input().split())

vogais = "aeiou"
plurais = {}

for _ in range (n):
    singular1, plural1 = input().split()
    plurais [singular1] = plural1

for _ in range (m):
    palavra = input()
    
    if palavra in plurais:
        print (plurais[palavra])
        
    else:
        if palavra.endswith(("o", "s", "ch", "sh", "x")):         
            concatenada = palavra + "es"
            print (concatenada)
            
        elif palavra.endswith("y") and palavra[-2] not in vogais:
            concatenada2 = palavra[:-1] + "ies"
            print (concatenada2)
            
        else:
            concatenada3 = palavra + "s"
            print (concatenada3)
