# -*- coding: utf-8 -*-
a, b, c = list(map(float, input().split()))

triangulo = (a * c) / 2 
circulo = 3.14159 * (c)**2
trapezio = ((a + b) * c) / 2
quadrado = b**2
retangulo = a * b 

print ("TRIANGULO: %.3f" % triangulo)
print ("CIRCULO: %.3f " % circulo)
print ("TRAPEZIO: %.3f" % trapezio)
print ("QUADRADO: %.3f" % quadrado)
print ("RETANGULO: %.3f" % retangulo)