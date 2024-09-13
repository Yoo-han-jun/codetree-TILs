n = int(input())
arr = [list(map(int,input().split())) for _ in range (n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n
max_val = 0
for i in range(n):
    for j in range(n):
        for k in range(i, n):
            if i==k:
                for l in range(j+3, n):
                    cnt= 0
                    if in_range(i,j) and in_range(i,j+2) and in_range(k,l) and in_range(k,l+2):
                        for m in range (3):
                            if arr[i][j+m]==1:
                                cnt+=1
                            if arr[k][l+m]==1:
                                cnt+=1
                    max_val = max(max_val, cnt)
            else:
                for l in range(n):
                    cnt= 0
                    if in_range(i,j) and in_range(i,j+2) and in_range(k,l) and in_range(k,l+2):
                            for m in range (3):
                                if arr[i][j+m]==1:
                                    cnt+=1
                                if arr[k][l+m]==1:
                                    cnt+=1
                    max_val = max(max_val, cnt)
print(max_val)