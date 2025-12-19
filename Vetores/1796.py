q = int(input())
v = list(map(int, input().split()))

y = 0 
n = 0 

for i in v:
    
    if i == 1:
        n += 1
        
    if i == 0:
        y += 1 

if n >= y:
    print ("N")
    
else:
    print ("Y")
