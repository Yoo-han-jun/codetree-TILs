n = int(input())
x,y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
mapper = {
    "W":2,
    "E":0,
    "N":1,
    "S":3
}
cnt = 0
answer = False
for _ in range(n):
    dir_c, t = tuple(input().split())
    t = int(t)
    for _ in range(t):
        x, y = x+dx[mapper[dir_c]], y+dy[mapper[dir_c]]
        cnt += 1
        if x==0 and y==0 :
            answer = True
            break
    if answer==True:
        print(cnt)
        break
if answer == False:
    print(-1)