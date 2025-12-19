# -*- coding: utf-8 -*-
n = int(input())

casa = 0 
trabalho = 0 

comprarcasa = 0 
comprartrabalho = 0 

for _ in range (n):
    sd, sn = input().split()
    
    if sd == "chuva": #se ta chovendo na ida
        if casa > 0: #se ja tem guarda chuvas em casa:
            casa -= 1 
            trabalho += 1 
        
        else:
            comprarcasa += 1 
            trabalho += 1 
        
    if sn == "chuva":
        if trabalho > 0 :
            trabalho -= 1 
            casa += 1 
            
        else:
            comprartrabalho += 1 
            casa += 1 
        
print (comprarcasa, comprartrabalho)
