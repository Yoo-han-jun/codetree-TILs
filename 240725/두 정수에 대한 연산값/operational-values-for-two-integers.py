a,b = map(int, input().split())
def t(a, b):
    if a>b:
        print(a+25, b*2)
    else:
        print(a*2, b+25)
t(a,b)