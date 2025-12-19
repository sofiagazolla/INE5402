# -*- coding: utf-8 -*-
while True:
    try:
        
        mes, dia = map(int,input().split())
        
        quantosmeses = 12 - mes - 1 
        
        quantosdias = 30 - dia
        
        total = quantosmeses * 30 + quantosdias + 25
        
        if mes == 1 or mes == 3:
            total += 5
        
        elif mes == 2 or mes == 4 or mes == 5:
            total += 4
        
        elif mes == 6 or mes == 7:
            total += 3
            
        elif mes == 8:
            total += 2
        
        elif mes == 9 or mes == 10:
            total += 1
        
        if quantosmeses == -1 and dia == 25:
            print ("E natal!")
            
        elif quantosmeses == -1 and quantosdias == 6:
            print ("E vespera de natal!")
            
        elif quantosmeses == -1 and dia != 24 and quantosdias != 6:
            print ("Ja passou!")
            
        else: 
            print ("Faltam %d dias para o natal!" % total)
        
    except EOFError:
        break
