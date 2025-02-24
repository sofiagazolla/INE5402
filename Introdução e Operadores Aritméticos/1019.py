tempo = int(input())

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60

print ("%d:%d:%d" % (horas,minutos,segundos))