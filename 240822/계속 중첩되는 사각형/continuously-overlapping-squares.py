MAX_R = 2001
os = 1000
arr = [[0 for _ in range (MAX_R)] for _ in range (MAX_R)]
n = int(input())
for i in range (n):
    x1, y1, x2, y2 = map(int,input().split())
    x1, y1, x2, y2 = x1+os, y1+os, x2+os, y2+os
    for k in range(x1, x2):
        for j in range (y1, y2):
            arr[k][j] = i
area = 0
for x in range (len(arr)):
    for y in range (len(arr[i])):
        if arr[x][y]%2==1:
            area+=1
print(area)