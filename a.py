import math
n = int (input())
for _ in range (n):
    a,b,c= map(int,input().split())
    if a<=3:
        print (a*b)
    else:
        if a %3==0:
            d=int((a/3)-1)*c+a*b
            print(d)
        else:
             d=int(a/3)*c+a*b
             print(d)