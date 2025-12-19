while True:
    try:
        A, B, C = input().split()
        A = int(A)
        B = int(B)
        C = int(C)
        
        if A != B and A != C and B == C:
            print ("A")
            
        elif A == B and B != C and A != C:
            print ("C")
            
        elif A == C and B != C and B != A:
            print ("B")
            
        else:
            print ("*")
            
    except EOFError:
        break
