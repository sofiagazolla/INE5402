def eh_primo(numero):

    if numero < 0:
        return False
    
    if numero <= 3:
        return True

    if numero % 2 == 0:
        return False

    if numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i+2) == 0:
            return False
        
        i += 6

    return True

casos = int(input())

for _ in range (casos):
    numero = int(input())
    
    if eh_primo(numero):
        print ("Prime")
    else:
        print("Not Prime")

