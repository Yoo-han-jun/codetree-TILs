a, b = map(int,input().split())
def s(M, D):
    if D<=31 and (M == 1 or 3 or 5 or 7 or 8 or 10 or 12):
        print("Yes")
    elif D<=30 and (M == 4 or 6 or 9 or 11):
        print("Yes")
    elif (M == 2 and D<=28):
        print("Yes")
    else:
        print("No")
s(a, b)