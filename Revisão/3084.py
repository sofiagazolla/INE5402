# -*- coding: utf-8 -*-
while True:
    try:
        entrada = input().split()
        
        if not entrada: # se estiver vazia
            break
            
        h_angulo = int(entrada[0])
        m_angulo = int(entrada[1])
        
        # cada hora equivale a 30 graus (360 / 12).
        horas = h_angulo // 30
        
        # cada minuto equivale a 6 graus (360 / 60).
        minutos = m_angulo // 6
        

        print(f"{horas:02d}:{minutos:02d}")
        
    except EOFError:
        break
