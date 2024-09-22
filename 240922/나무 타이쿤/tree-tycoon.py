n, m = map(int,input().split())

# 이동방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

farm = [list(map(int,input().split())) for _ in range (n)]
eat = [[0 for _ in range (n)] for _ in range (n)]
eat2 = [[0 for _ in range (n)] for _ in range (n)]
eat_final = [[0 for _ in range (n)] for _ in range (n)]
dir_c = []
rp = []
sum_val = 0
for _  in range (m):
    d, p = map(int,input().split())
    dir_c.append(d)
    rp.append(p)
# 초기 eat:
eat[n-1][1] = 1
eat[n-1][0] = 1
eat[n-2][1] = 1
eat[n-2][0] = 1

def in_range (x,y):
    return x>=0 and x<n and y>=0 and y<n

def out_range(x,y):
    if x>=n and y>=n:
        return x%n, y%n
    if x>=n and y<0:
        return x%n, y+n
    if x<0 and y>=0:
        return x+n, y%n
    if x<0 and y<0:
        return x+n, y+n
    if y<0:
        return x, y+n
    if y>=n:
        return x, y%n
    if x<0:
        return x+n, y
    if x>=n:
        return x%n, y

# p = 홀수 / eat2 p=짝수 / eat
for i in range (m):
    for l in range (rp[i]):
        if l%2 == 0:
            for j in range(n):
                for k in range(n): 
                    if eat[j][k]==1:
                        dxs, dys = j+dx[dir_c[i]-1], k+dy[dir_c[i]-1]
                        if not in_range(dxs, dys):
                            dxs, dys = out_range(dxs, dys)
                        eat2[dxs][dys] =1
                        eat[j][k] = 0
        if l%2 ==1:
            for j in range(n):
                for k in range(n): 
                    if eat2[j][k]==1:
                        dxs, dys = j+dx[dir_c[i]-1], k+dy[dir_c[i]-1]
                        if not in_range(dxs, dys):
                            dxs, dys = out_range(dxs, dys)
                        eat[dxs][dys] =1
                        eat2[j][k] = 0
    if rp[i]%2==1:
        for y in range (n):
            for u in range (n):
                eat_final[y][u] = eat2[y][u] 
    if rp[i]%2==0:
        for y in range (n):
            for u in range (n):
                eat_final[y][u] = eat[y][u] 

    
    # 성장
    for s in range(n):
        for p in range(n):
            if eat_final[s][p]==1:
                farm[s][p] = farm[s][p] +1

    for s in range(n):
        for p in range(n):
            if eat_final[s][p]==1:            
                cnt = 0
                for q in range (1, 8, 2):
                    dxs , dys = s+dx[q], p+dy[q]
                    if in_range(dxs, dys) and farm[dxs][dys]>=1:
                        cnt+=1
                farm[s][p] = farm[s][p] +cnt
 
    # 커팅
    eat = [[0 for _ in range (n)] for _ in range (n)]
    eat2 = [[0 for _ in range (n)] for _ in range (n)]

    for w in range(n):
        for e in range(n):
            if farm[w][e]>=2 and eat_final[w][e]==0:
                farm[w][e] = farm[w][e]-2
                eat[w][e] =1
    eat_fianl = [[0 for _ in range (n)] for _ in range (n)]

for i in range(n):
    for j in range (n):
        sum_val += farm[i][j]
print(sum_val)