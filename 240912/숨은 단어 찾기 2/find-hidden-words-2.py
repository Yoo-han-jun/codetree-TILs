n, m =map(int,input().split())
arr = [tuple(input())for _ in range (n)]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
cnt = 0
def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m
for i in range (n):
    for j in range (m):
        if arr[i][j] =="L":
            for k in range (8):
                dxs, dys = i+dx[k], j+dy[k]
                dxs2, dys2 = dxs+dx[k], dys+dy[k]
                if not in_range(dxs, dys) or not in_range(dxs2, dys2):
                    continue
                if arr[dxs][dys]=="E" and arr[dxs2][dys2]=="E":
                    cnt+=1
print(cnt)