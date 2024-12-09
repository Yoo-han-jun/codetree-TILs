a, b, c = map(int,input().split())
d = c//a
e = c//b
max_cnt = 0
for i in range (d):
    cnt = 0
    for j in range (e):
        cnt = i*a+j*b
        if cnt<=c:
            max_cnt = max(cnt, max_cnt)
print(max_cnt)
