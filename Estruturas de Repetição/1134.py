a = 0 
b = 0 
c = 0 

while True:
    N = int(input())
    
    if N == 1:
        a += 1 
        
    elif N == 2:
        b += 1 
        
    elif N == 3:
        c += 1 
        
    elif N == 4:
        break
    
print ("MUITO OBRIGADO")
print ("Alcool: %d" % (a))
print ("Gasolina: %d" % (b))
print ("Diesel: %d" % (c))
