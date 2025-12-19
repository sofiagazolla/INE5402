# -*- coding: utf-8 -*-
n = int(input())

tempo_total = 0
instante_anterior = None

for i in range(n):
    instante_atual = int(input())
    
    if i == 0:
        # a primeira pessoa ativa a escada por pelo menos 10s
        tempo_total = 10
    else:
        diferenca = instante_atual - instante_anterior
        
        if diferenca >= 10:
            # se a diferença for 10 ou mais funcionou 10s a mais 
            tempo_total += 10
        else:
            # se for menor que 10 funcionou apenas o tempo da diferença
            tempo_total += diferenca
            
    # guarda o instante atual para comparar com o próximo
    instante_anterior = instante_atual

print(tempo_total)
