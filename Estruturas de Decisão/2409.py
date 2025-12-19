a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
h, l = input().split()
h = int(h)
l = int(l)

c1 = (a <= h and b <= l) or (a <= l and b <= h)
c2 = (a <= h and c <= l) or (a <= l and c <= h)
c3 = (b <= h and c <= l) or (b <= l and c <= h)

if c1 or c2 or c3:
    print ("S")
    
else:
    print ("N")
