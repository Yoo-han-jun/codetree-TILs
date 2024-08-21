n = int(input())
cnt = 0
arr = [[0 for _ in range (201) ] for _ in range (201)]
offset = 100
for _ in range (n):
    a, b = map(int,input().split())
    a, b= a+offset, b+offset
    for i in range (a, a+8):
        for j in range (b, b+8):
            arr[i][j] = 1
for i in range (len(arr)):
    for j in range (len(arr[i])):
        if arr[i][j]==1:
            cnt+=1
print(cnt)