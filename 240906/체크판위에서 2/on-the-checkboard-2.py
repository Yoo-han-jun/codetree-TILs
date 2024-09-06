n, m = map(int, input().split())
arr = [list(map(str,input().split())) for _ in range (n)]
sum_val = 0
for i in range(1, n-1):
    for j in range (1, m-1):
        arr[i][j]!=arr[0][0]
        if arr[i][j] == arr[n-1][m-1]:
            for k in range(i+1, n-1):
                for l in range(j+1, m-1):
                    if arr[k][l] != arr[i][j]:
                        sum_val+=1
print(sum_val)