a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a < b and a < c:
    print("Otavio")
    
elif b < a and b < c:
    print("Bruno")
    
elif c < a and c < b:
    print("Ian")
    
else:
    print("Empate")
