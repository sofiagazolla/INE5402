# -*- coding: utf-8 -*-
diasmes = { 1 : 31, 2 : 28, 3: 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 
8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31 }

total = 0 

dia, mes = list(map(int, input().split()))
dia2, mes2 = list(map(int, input().split()))

if mes < mes2 or (mes == mes2 and dia < dia2):
    #conta os dias dos meses entre as duas datas
    meses = list(range(mes+1, mes2))
    for m in meses:
        total += diasmes[m] 
    
    total += diasmes[mes] - dia
    total += dia2
        
elif mes > mes2 or (mes == mes2 and dia > dia2):
    #conta os dias dos meses da primeira data até o final do ano
    meses = list(range(mes+1, 13))
    for m in meses:
        total+= diasmes[m]
    
    #conta os dias dos meses do começo do ano até a segunda data
    meses = list(range(1, mes2)) 
    for m in meses:
        total+= diasmes[m]
    
    total += diasmes[mes] - dia
    total += dia2
    
else: # se as datas forem iguais
    total = 0 
    
print (total)
