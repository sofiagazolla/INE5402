N = int(input())

for _ in range (0,N):
    x, y = input().split()
    x = int(x)
    y = int(y)
    
    r = ((3*x)**2) + y**2
    b = (2*(x**2)) + (5*y)**2
    c = (-100*x) + y**3
    
    if r > b and r > c:
        print ("Rafael ganhou")
        
    elif b > r and b > c:
        print ("Beto ganhou")
        
    else:
        print ("Carlos ganhou")
