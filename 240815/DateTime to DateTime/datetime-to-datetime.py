a, b, c = list(map(int,input().split()))
cnt = 11*24*60+11*60+11
cnt -= (a*24*60+b*60+c)
if cnt>0:
    print(-1)
else:
    print(abs(cnt))