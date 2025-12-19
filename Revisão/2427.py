# -*- coding: utf-8 -*-
lado = int(input())

total_pedacos = 1

while lado >= 2:
    # lado é reduzido pela metade a cada divisão
    lado = lado // 2
    
    # cada pedaço existente se divide em 4 novos pedaços
    total_pedacos = total_pedacos * 4

print(total_pedacos)
