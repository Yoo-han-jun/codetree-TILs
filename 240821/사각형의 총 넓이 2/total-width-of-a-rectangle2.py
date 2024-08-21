n = int(input())
cnt=0
arr = [[0 for j in range(10)] for i in range(10)]
for _ in range (n):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j]=1
for i in range (len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]==1:
            cnt+=1
print(cnt)