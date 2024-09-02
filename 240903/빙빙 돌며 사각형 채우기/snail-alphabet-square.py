# A = chr(65) Z = chr(65+25)
n, m = map(int,input().split())
arr = [[0 for _ in range (m)] for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

dir_c = 0
r, c= 0, -1
def in_range(r,c):
    return r>=0 and r<n and c>=0 and c<m

for i in range (n*m):
    drs, dcs = r+dr[dir_c], c+dc[dir_c]
    if not in_range(drs,dcs) or arr[drs][dcs]!=0:
        dir_c = (dir_c+1)%4
        c, r = c+dc[dir_c], r+dr[dir_c]
        arr[r][c] = chr(65+(i%26))
    elif in_range(drs,dcs):
        c, r = c+dc[dir_c], r+dr[dir_c]
        arr[r][c] = chr(65+(i%26))


for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()