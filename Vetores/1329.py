while True:
    n = int(input())
    if n == 0:
        break

    ri = list(map(int, input().split()))

    m = 0 
    j = 0 
    
    for i in ri:
        
        if i == 0:
            m += 1 
            
        elif i == 1:
            j += 1

    print("Mary won %d times and John won %d times" % (m, j))
