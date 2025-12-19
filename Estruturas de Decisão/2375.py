N = float(input())
A, L, P = input().split()
A = float(A)
L = float(L)
P = float(P)

if N <= A and N <= L and N <= P:
    print('S')

else:
    print('N')
