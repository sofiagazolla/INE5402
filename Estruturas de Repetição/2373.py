N = int(input())

Q = 0 

for _ in range (0,N):
    L,C = input().split()
    L = int(L)
    C = int(C)
    if L > C: 
        Q += C 
    
print ("%d" % (Q))
