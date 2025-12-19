import math

while True:
    try: 
        a, b, c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        
        s = (a + b + c) / 2 
        
        at = math.sqrt(s * (s-a) * (s-b) * (s-c))
        
        r = at / s 
        
        ac = math.pi * (r ** 2)
        
        atf = at - ac 
        
        r2 = (a * b * c) / (4 * at)
        
        ac2 = (math.pi * (r2 ** 2) ) - at
        
        print ("%.4f %.4f %.4f" % (ac2, atf, ac) ) 
    
    except EOFError:
        break
