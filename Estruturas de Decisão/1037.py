# -*- coding: utf-8 -*-
X = float(input())

if X >= 0 and X <= 25.0000:
  print (f"Intervalo [0,25]")
  
elif X > 25.0000 and X <= 50.0000:
    print (f"Intervalo (25,50]")
    
elif X > 50.0000 and X <= 75.0000:
    print (f"Intervalo (50,75]")
    
elif X > 75.0000 and X <= 100.0000:
    print (f"Intervalo (75,100]")
    
else:
    print (f"Fora de intervalo")
    
