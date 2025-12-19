n = int(input())

for i in range (n):
    a, b = map(int, input().split())
    
    x = min(a,b)
    y = max(a,b)
    
    soma = 0 
    for i in range (x,y):
        if i > x and i < y and i % 2 == 1:
            soma += i 

    print (soma)
