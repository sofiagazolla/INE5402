A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

if A > B and B > C or C > B and B > A:
    print (f"{B}")
    
elif B > A and A > C or C > A and A > B:
    print (f"{A}")
    
elif A > C and C > B or B > C and C > A:
    print (f"{C}")
