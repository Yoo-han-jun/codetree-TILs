n, d = map(int,input().split())
dr = tuple(input())
x, y = n//2 , n//2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir_c = 0
arr = [list(map(int, input().split()))for _ in range (n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n
sum = arr[x][y]
for i in range (d):
    if dr[i] == "L":
        dir_c = (dir_c+3)%4
    if dr[i] == "R":
        dir_c = (dir_c+1)%4
    if dr[i] == "F":
        dxs, dys = x +dx[dir_c], y+dy[dir_c]
        if in_range(dxs, dys):
            x, y = x+ dx[dir_c], y+dy[dir_c]
            sum += arr[x][y]

print(sum)