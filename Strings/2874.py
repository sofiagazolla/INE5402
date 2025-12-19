while True:
    try:
        numeros = int(input())
        
        palavra = []
        
        for i in range (numeros):
            binario = input()
        
            decimal = int(binario, 2)
            
            hexa = hex(decimal)[2:]
            
            caractere = chr(int(hexa,16))
            
            palavra.append(caractere)
        
        print ("".join(palavra))
    
    except EOFError:
        break
