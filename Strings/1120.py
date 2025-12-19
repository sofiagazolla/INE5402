while True:
    num, lista = input().split()
    num = int(num)
    
    if num == 0 and lista == "0":
        break

    final = lista.replace(str(num), "")
    
    if final == "":
        print ("0")
    
    else:
        print(str(int(final)))
        
