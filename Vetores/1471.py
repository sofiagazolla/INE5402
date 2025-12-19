# -*- coding: utf-8 -*-
while True:
    try: 
        n, r = map(int,input().split())
        
        retornaram = input().split()
        if r == n:
            print("*")
            
        else:
            nv = [True] * (n+1) 
            for i in range(r):
                nv [int(retornaram [i])] = False
                
            for i in range (1, n+1):
                if nv[i]: 
                    print ("%d " % i, end="")
                    
            print ()
        
    except EOFError:
        break
