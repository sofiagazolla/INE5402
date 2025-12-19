x = True

while True:
    try: 
        N = int(input())
        if x:
             x = False
        else: 
            print ()
        leap = (N % 4 == 0 and N % 100 != 0) or (N % 400 == 0)
            
        hulu = (N % 15 == 0)
            
        bulu = leap and (N % 55 == 0)
        
        if leap:
            print ("This is leap year.")
            
        if hulu:
            print ("This is huluculu festival year.")
            
        if bulu: 
            print ("This is bulukulu festival year.")
            
        if not (leap or hulu or bulu):
            print ("This is an ordinary year.")
            
        
    except EOFError:
        break 
