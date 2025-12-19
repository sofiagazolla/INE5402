n = int(input())
m = input().split()

for h in m:
    
        i = int(h,16) #converte hexa para decimal
        a = chr(i) #converte para caractere
        print (a, end = "")

print ()
