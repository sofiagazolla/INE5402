# -*- coding: utf-8 -*-
a, b, c, d = input().split()
a = float(a)
b = float(b)
c = float(c)
d = float(d)

m = ((a*2) + (b*3) + (c*4) + d) / 10

if m >= 7:
    print("Media: %.1f" % m)
    print("Aluno aprovado.")
elif m < 5:
    print("Media: %.1f" % m)
    print("Aluno reprovado.")

else:
    print("Media: %.1f" % m)
    print("Aluno em exame.") 
    e = float(input())
    print("Nota do exame: %.1f" % e)
    
    m2 = (m + e) / 2
    
    if m2 >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print("Media final: %.1f" % m2)
