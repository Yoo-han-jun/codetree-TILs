dir_num = 3
x, y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
arr = ["E","S","W","N"]
n = tuple(input())
#오른쪽 90도 동남서북 4
#왼쪽 90도 동북서남
for i in range (len(n)):
    if n[i] == "L":
        dir_num = (dir_num+3)%4
    if n[i] == "R":
        dir_num = (dir_num+1)%4
    if n[i] == "F":
        x, y = x+dx[dir_num], y+dy[dir_num]
print(x, y)