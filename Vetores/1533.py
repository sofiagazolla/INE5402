# -*- coding: utf-8 -*-
while True:
    n = int(input()) 
    if n == 0:
        break
    
    s = input().split()
    
    m = 0 
    sm = 0 
    p1 = 0 
    p2 = 0 
    
    for i in range (0,n):
        
        s[i] = int(s[i])
        
        if s[i] > m:
            sm = m
            m = s[i]
            
            p2 = p1 
            p1 = i 
            
        elif s[i] > sm:
            p2 = i 
            sm = s[i]
            
    print("%d" % (p2 + 1))
