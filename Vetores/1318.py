while True:
    
    n, m = input().split()
    n = int(n) #numero de bilhetes originais
    m = int (m) #numero de pessoas na festa
    
    if n == 0 and m == 0:
        break
    
    bilhetes = input().split()
    contagem = [0] * (n+1) 
    for i in range (m):
        contagem [int(bilhetes[i])] += 1  #verifica quantos bilhetes de cada número tem
        
    falsos = 0 
    
    for i in range (n+1):
        if contagem[i] > 1: #se tiver mais de um bilhete de cada número, incrementa o número de bilhetes falsos em 1
            falsos += 1 
            
    print(falsos)
