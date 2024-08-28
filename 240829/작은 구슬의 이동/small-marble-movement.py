n, t = map(int,input().split())
arr = [[0 for _ in range (n)] for _ in range (n)]
x, y, D = tuple(input().split())
x, y = int(x), int(y)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
mapper = {
    'U' : 0,
    'R' : 1,
    "D" : 2,
    "L" : 3
}
cnt = 0
#1 내부 확인
def in_range(x, y):
    return x>0 and x<=n and y>0 and y<=n
#2 방향 및 위치 확인
dir_c = mapper[D]
nx, ny = x, y
while True:
    nx, ny = nx + dx[dir_c], ny + dy[dir_c] 
    if in_range(nx,ny) == False:
        nx, ny = nx-dx[dir_c], ny - dy[dir_c]
        dir_c = (dir_c+2)%4
        cnt+=1
    elif in_range(nx,ny) == True:
        cnt+=1
    if cnt==t:
        break
print(nx, ny)