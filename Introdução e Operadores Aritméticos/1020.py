total = int(input())

ano = total // 365
mes = (total % 365) // 30
dia = (total % 365) % 30

print ("%d ano(s)" % ano)
print ("%d mes(es)" % mes)
print ("%d dia(s)" % dia)