l, a, p, r = input().split()
l = int(l)
a = int(a)
p = int(p)
r = int(r)

if ((l**2 + a**2 + p**2)**0.5) <= 2*r:
    print("S")

else:
    print("N")
