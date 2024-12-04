n = int(input())
max_cnt = 0
arr = [list(map(int,input().split())) for _ in range (n)]
for j in range (3):
    cnt = 0
    arr2 = [0, 0, 0]
    arr2[j] = 1
    for i in range (n):
        a, b = arr2[arr[i][0]-1], arr2[arr[i][1]-1]
        arr2[arr[i][0]-1] = b
        arr2[arr[i][1]-1] = a
        if arr2[arr[i][2]-1]==1:
            cnt+=1
    max_cnt = max(cnt, max_cnt)
print(max_cnt)