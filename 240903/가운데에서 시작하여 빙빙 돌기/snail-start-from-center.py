n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
x, y = n-1, n
dir_c = 0
def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

for i in range(n*n, 0, -1):
    dxs, dys = x + dx[dir_c], y+dy[dir_c]
    if not in_range(dxs, dys) or arr[dxs][dys]!=0:
        dir_c = (dir_c+1)%4
    x, y = x+dx[dir_c], y+dy[dir_c]
    arr[x][y] = i

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()