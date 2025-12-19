N1, D1, V1 = input().split()
N1 = int(N1)
D1 = int(D1)
V1 = int(V1)
N2, D2, V2 = input().split()
N2 = int(N2)
D2 = int(D2)
V2 = int(V2)

V3 = V1/3.6
V4 = V2/3.6

T1 = D1/V3
T2 = D2/V4

if T1 < T2:
    print(f"{N1}")
    
elif T2 < T1:
    print(f"{N2}")
