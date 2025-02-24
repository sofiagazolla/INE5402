a,b,c = map(int,input().split())
x,y,z = map(int,input().split())

total = (x // a) * (y//b) * (z // c)

if c <= z:
    print (total)

else: 
    print ("0")