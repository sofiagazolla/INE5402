n = int(input())

for _ in range (n):
    a = int(input())
    b, c, d, e = map(int,input().split())
    f = int(input())
    
    dado = [a, b, c, d, e, f]
    
    if sorted(dado) != [1, 2, 3, 4, 5, 6]:
        print ("NAO")
        
    else:
    
        if a + f == 7 and b + d == 7 and c + e == 7:
            print ("SIM")
            
        else:
            print ("NAO")
