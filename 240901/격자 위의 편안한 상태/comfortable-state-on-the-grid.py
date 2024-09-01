n, m = map(int, input().split())
arr = [[0 for _ in range (n)] for _ in range (n)]
dx = [1, 0 , -1, 0]
dy = [0, 1 , 0 , -1]
cnt_safe = 0
def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

for _ in range (m):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    arr[x][y]=1
    cnt_color = 0
    for i in range (4):
        dxs, dys = x+dx[i], y+dy[i]
        if in_range(dxs,dys) and arr[dxs][dys]==1:
            cnt_color+=1
    if cnt_color ==3:
        print(1)
    else:
        print(0)