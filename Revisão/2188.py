teste = 1

while True:
    n = int(input())
    
    if n == 0:
        break
    
    # inicializa os limites da interseção com valores extremos
    x_final = -10001
    y_final = 10001
    u_final = 10001
    v_final = -10001
    
    for _ in range(n):
        x, y, u, v = map(int, input().split())
        
        # atualiza os limites conforme os novos retângulos
        if x > x_final: x_final = x
        if y < y_final: y_final = y
        if u < u_final: u_final = u
        if v > v_final: v_final = v
        
    print(f"Teste {teste}")
    
    # se a esquerda for menor que a direita e o topo maior que a base, há interseção
    if x_final < u_final and y_final > v_final:
        print(f"{x_final} {y_final} {u_final} {v_final}")
    else:
        print("nenhum")
        
    print() 
    teste += 1
