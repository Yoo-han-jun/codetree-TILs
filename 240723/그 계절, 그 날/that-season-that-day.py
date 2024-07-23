def s(Y, M, D):
    arr31 = [1, 3, 5, 7, 8, 10, 12]
    arr30 = [4, 6, 9, 11]
    if (Y%4==0 and Y%100!=0) or Y%400==0:
        if (D<=31 and (M in arr31)) or (D<=30 and (M in arr30)) or (D<=29 and M==2):
            if M>=3 and M<6:
                print("Spring")
            elif M>=6 and M<9:
                print("Summer")
            elif M>=9 and M<12:
                print("Fall")
            elif M==12 or M==1 or M==2:
                print("Winter")
        else:
            print(-1)
    else:
        if (D<=31 and (M in arr31)) or (D<=30 and (M in arr30)) or (D<=28 and M==2):
            if M>=3 and M<6:
                print("Spring")
            elif M>=6 and M<9:
                print("Summer")
            elif M>=9 and M<12:
                print("Fall")
            elif M==12 or M==1 or M==2:
                print("Winter")
        else:
            print(-1)
Y, M, D = map(int, input().split())
s(Y, M, D)