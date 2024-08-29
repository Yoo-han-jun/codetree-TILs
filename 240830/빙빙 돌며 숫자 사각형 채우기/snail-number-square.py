n, m = map(int,input().split())
arr = [[0 for _ in range (n)] for _ in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
nx, ny = 0, 0
dir_c = 0
cnt = 1
arr[nx][ny]=1

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

for i in range (2, n*m+1):
        nx, ny = x +dx[dir_c], y+dy[dir_c]
        if not in_range(nx,ny) or arr[nx][ny] !=0:
            dir_c = (dir_c+1)%4
        x, y = x+dx[dir_c], y+dy[dir_c]
        arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()