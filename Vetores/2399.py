n = int(input())

casinha = [""] * n #cria uma lista do tamanho de n para armazenar os resultados

for i in range (n): #é cada uma das n linhas da entrada
    casinha[i] = input()

total = [0] * n # armazena a contagem de bombas e ela é *n para que seja criado uma lista começando em 0 para cada elemento

for i in range (n):
    bombas = 0 
    
    if casinha[i] == "1":
        bombas += 1 
        
    if i < n-1 and casinha[i+1] == "1":
        bombas += 1 
        
    if i > 0 and casinha[i-1] == "1":
        bombas += 1 
        
    total[i] = bombas
    
for s in total:
    print (s)
