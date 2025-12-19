A, B, C, D = input().split()
A = float(A)
B = float(B)
C = float(C)
D = float(D)

if B > C and D > A and (C+D > A+B) and C > 0 and D > 0 and (A%2 == 0):
  print(f"Valores aceitos")

else:
    print(f"Valores nao aceitos")
