r , c = map(int,input().split())
a = [list(map(str, input().split())) for _ in range (r)]
x1, y1 = 0, 0
x2, y2 = 0, 0
for i in range (r):
    for j in range (c):
        if x2 == 0 and y2==0 and a[i][j] == "B":
            x2, y2 = i, j
        if a[i][j] == "B":
            x1, y1 = i, j
        
if (x1==0 and y1==0) or (x2==0 and y2==0):
    print(0)
else:
    print((x1-x2-1)*(y1-y2-1))