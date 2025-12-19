N = int(input())

for _ in range(1, N + 1):
    C = float(input())
    d = 0 
    
    while C > 1:
        C /= 2  
        d += 1  
        
    print("%d dias" % d)  
