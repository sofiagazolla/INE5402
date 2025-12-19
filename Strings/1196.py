teclado = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

while True:
    try:
        frase = input()
        traducao = ""
        
        for char in frase:
            if char == " ":
                traducao += " "
            else:
                # encontramos a posição do caractere no teclado e pegamos o caractere em index - 1
                posicao = teclado.find(char)
                traducao += teclado[posicao - 1]
        
        print(traducao)
        
    except EOFError:
        break
