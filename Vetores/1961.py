# -*- coding: utf-8 -*-
p, c = input().split()
p = int(p)
c = int(c)
x = list(map(int, input().split()))

w = True
for i in range (1,c):
    d = (x[i] - x[i-1])
        
    if abs (d) > p:
        w = False
        break
   
if w:
    print ("YOU WIN")
    
else:
    print("GAME OVER")
