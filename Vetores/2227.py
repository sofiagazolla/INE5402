teste = 1 

while True:
    
    a, v = input().split()
    a = int(a)
    v = int(v)
    
    if a == 0 and v == 0:
        break
    
    print ("Teste %d" % teste)
    teste += 1 
    
    voos = [0] * (a+1)
    
    for _ in range (v):
        x, y = input().split()
        x = int(x)
        y = int(y)
        
        voos[x] += 1 
        voos[y] += 1 
        
    maximo = 0 
    for i in range (a+1):
        if voos [i] > maximo:
            maximo = voos[i]
            
    for i in range (1,a+1): 
        if voos[i] == maximo:
            print (i, end=" ")
            
    print ()
    print ()
