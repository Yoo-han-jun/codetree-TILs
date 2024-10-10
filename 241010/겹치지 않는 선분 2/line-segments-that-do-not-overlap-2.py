n = int(input())
arr = [tuple(map(int,input().split())) for _ in range (n)]
cnt = 0
for i in range (n):
    union = False
    x1, x2 = arr[i]
    for j in range (n):
        if i==n:
            continue
        x3, x4 = arr[j]
        if (x3-x1)*(x4-x2)<0:
            union = True
    if union == False:
        cnt+=1
print(cnt)