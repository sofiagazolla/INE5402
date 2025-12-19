a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Valido-Equilatero")
        print("Retangulo: N")
    elif a == b or a == c or b == c:
        print("Valido-Isoceles")
        print("Retangulo: N")
    else:
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            print("Valido-Escaleno")
            print("Retangulo: S")
        else:
            print("Valido-Escaleno")
            print("Retangulo: N")
else:
    print("Invalido")
