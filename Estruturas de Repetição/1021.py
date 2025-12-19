# -*- coding: utf-8 -*-
v = float(input())

c = (v * 100) + 0.5

n = [10000, 5000, 2000, 1000, 500, 200]
m = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for ns in n:
    qn = (c // ns) 
    c %= ns 
    print ("%d nota(s) de R$ %.2f" % (qn,ns/100))
    
print("MOEDAS:")
for ms in m:
    qm = (c // ms)
    c %= ms 
    print ("%d moeda(s) de R$ %.2f" % (qm,ms/100))
