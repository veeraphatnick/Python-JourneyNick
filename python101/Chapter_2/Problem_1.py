a,b,c = [int(e) for e in input().split()]
if(b <= a <=c or c <= a <= b):
    print(a)
elif(a <= b <= c or c <= b <= a):
    print(b)
else:
    print(c)