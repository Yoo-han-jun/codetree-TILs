a, b = map(int,input().split())
def s(M, D):
    if (M == (1 or 3 or 5 or 7 or 8 or 10 or 12)) and D<=31:
        print("Yes")
    elif (M == (4 or 6 or 9 or 11)) and D<=30:
        print("Yes")
    elif M == 2 and D<=28:
        print("Yes")
    else:
        print("No")
s(a, b)