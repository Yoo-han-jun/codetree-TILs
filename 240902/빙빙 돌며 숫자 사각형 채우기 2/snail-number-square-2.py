n, m = map(int, input().split())
arr = [[0 for _ in range (m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x,y = -1, 0
dir_c = 0
def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

for i in range(1, m*n+1):
    dxs, dys = x+dx[dir_c], y+dy[dir_c]
    if not in_range(dxs,dys) or arr[dxs][dys]!=0:
        dir_c = (dir_c+1)%4
        x, y = x+dx[dir_c], y+dy[dir_c]
        arr[x][y]=i
    elif in_range(dxs,dys):
        x, y = x+dx[dir_c], y+dy[dir_c]
        arr[x][y]=i

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()