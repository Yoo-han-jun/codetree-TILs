dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y = 0,0
n = int(input())
for i in range (n):
    a, b= input().split()
    if a=="N":
        dir_c = 1
    if a=="E":
        dir_c = 0
    if a=="W":
        dir_c = 2
    if a=="S":
        dir_c = 3
    b = int(b)
    for i in range (b):
        x, y = x+dx[dir_c], y+dy[dir_c]
print( x, y)