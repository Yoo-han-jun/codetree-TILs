n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
# Please write your code here.
for i in range(n-2):
    for j in range (n-2):
        cnt = 0
        for k in range (i, i+3):
            for l in range (j, j+3):
                if gird[k][l]==1:
                    cnt+=1
        max_cnt = max(max_cnt, cnt)

print(max_cnt)