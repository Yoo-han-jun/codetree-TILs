def m(a,b):
    if a>b:
        return 2*a , b+10
    else:
        return a+10, 2*b
a, b = map(int,input().split())
c, d = m(a,b)
print(c, d)