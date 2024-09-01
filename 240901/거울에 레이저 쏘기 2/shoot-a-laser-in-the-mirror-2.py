# "\-b" {0-1}, {2-3} "a" {0-3} {1-2}
dx = [0, 1, 0, -1]
dy = [1, 0, -1 , 0]
ox, oy = 0,0
dir_d = 0
mappera = {
    0:3,
    3:0,
    1:2,
    2:1
}

mapperb = {
    0:1,
    1:0,
    2:3,
    3:2
}
cnt = 1
n = int(input())
arr = [[0 for _ in range(n+2)] for _ in range (n+2)]
for i in range (1,n+1):
    sp = tuple(input())
    for j in range (n):
        if sp[j] == "/" :
            arr[i][j+1]="a"
        else:
            arr[i][j+1]="b"
m = int(input())

def in_range_out(x,y):
    return x>=0 and x<n+2 and y>=0 and y<n+2

def in_range_light(x,y):
    return x>=1 and x<n+1 and y>=1 and y<n+1


for _ in range (4*n+8):
    dirx, diry = ox+dx[dir_d], oy+dy[dir_d]
    if in_range_out(dirx,diry) == False:
        dir_d = (dir_d+1)%4
    else:
       ox, oy = ox +dx[dir_d], oy+dy[dir_d]
       if abs(ox-oy) == n+1 or ox == oy:
        arr[ox][oy] == 0
       else:
        arr[ox][oy] = cnt
        if cnt == m:
            break
        cnt+=1
dir_l = (dir_d+1)%4
cnt2 = 0        
while True:
    dirx, diry = ox+dx[dir_l], oy+dy[dir_l]
    if not in_range_light(dirx,diry):
        print(cnt2)
        break
    else:
        ox, oy = ox+dx[dir_l], oy+dy[dir_l]
        if arr[ox][oy] == "a":
            dir_l = mappera[dir_l]
        if arr[ox][oy] == "b":
            dir_l = mapperb[dir_l]
        cnt2+=1