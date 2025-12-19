x, y = map(int, input().split()) # dimensões da página

l1, h1 = map(int, input().split()) # dimensões da primeira foto

l2, h2 = map(int, input().split()) # dimensões da segunda foto

def verificar(pag_x, pag_y, f1_l, f1_h, f2_l, f2_h):
    
    # tenta colocar uma do lado da outra
    if (f1_l + f2_l <= pag_x) and (max(f1_h, f2_h) <= pag_y):
        return True
    
    # tenta colocar uma em cima da outra
    if (f1_h + f2_h <= pag_y) and (max(f1_l, f2_l) <= pag_x):
        return True
        
    return False

possivel = False

# combinação 1: foto 1 normal, foto 2 normal
if verificar(x, y, l1, h1, l2, h2):
    possivel = True

# combinação 2: goto 1 girada, foto 2 normal
elif verificar(x, y, h1, l1, l2, h2):
    possivel = True

# combinação 3: foto 1 normal, foto 2 girada
elif verificar(x, y, l1, h1, h2, l2):
    possivel = True

# combinação 4: foto 1 girada, foto 2 girada
elif verificar(x, y, h1, l1, h2, l2):
    possivel = True

if possivel:
    print("S")
else:
    print("N")
