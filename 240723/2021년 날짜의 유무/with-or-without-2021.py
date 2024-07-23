a, b = map(int,input().split())
def s(M, D):
    if D<=31 and (M == 1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12):
        print("Yes")
    elif D<=30 and (M == 4 or M==6 or M==9 or M==11):
        print("Yes")
    elif (M == 2 and D<=28):
        print("Yes")
    else:
        print("No")
s(a, b)