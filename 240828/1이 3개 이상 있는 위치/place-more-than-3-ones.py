n = int(input())
narr = []
for _ in range (n):
    arr = list(map(int,input().split()))
    narr.append(arr)
dxs = [1, -1, 0, 0]
dys = [0, 0 , 1, -1]

tnum = 0
def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n
for i in range(n):
    for j in range(n):
        cnt = 0
        for a, b in zip (dxs, dys):
            nx, ny = i+a, j+b
            if in_range(nx,ny) and narr[nx][ny]==1:
                cnt+=1
        if cnt>=3:
            tnum+=1
print(tnum)