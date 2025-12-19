A, B, C = input (). split ()
A = float(A)
B = float(B)
C = float(C)

if A + B > C and B + C > A and A + C > B: 
    print(f"Perimetro = {A+B+C:.1f}")
    
else:
    print(f"Area = {((A+B)*C)/2:.1f}")
    
