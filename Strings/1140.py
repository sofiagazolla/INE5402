# -*- coding: utf-8 -*-
while True:
    frase = input().strip()
    
    if frase == '*':
        break
    
    palavras = frase.split()
    
    primeira = palavras[0][0].lower()
    
    comecam = True
    for palavra in palavras:
        if not palavra.lower().startswith(primeira):
            comecam = False
            break
        
    if comecam:
        print ("Y")
    else: 
        print ("N")
