x = int(input())

for _ in range (0,x):

    N = int(input())
    
    if N > 0 and N % 2 == 0:
        print ("EVEN POSITIVE")
    elif N > 0 and N % 2 != 0: 
        print ("ODD POSITIVE")
    elif N < 0 and N % 2 == 0:
        print ("EVEN NEGATIVE")
    elif N < 0 and N % 2 != 0:
        print ("ODD NEGATIVE")
    else:
        print ("NULL")
