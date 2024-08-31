n = tuple(input())
x, y = 0,0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
dir_c = 3
cnt = 0
answer = False
for i in range(len(n)):
    if n[i] =="L":
        dir_c = (dir_c+3)%4
        cnt +=1
    if n[i] =="R":
        dir_c = (dir_c+1)%4
        cnt +=1
    if n[i] =="F":
        x, y = x+dx[dir_c], y+dy[dir_c]
        cnt+=1
    if x==0 and y==0:
        answer = True
        break
if answer == True:
    print(cnt)
else:
    print(-1)