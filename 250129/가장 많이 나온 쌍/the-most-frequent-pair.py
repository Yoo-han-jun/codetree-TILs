n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]
max_val = 0
# Write your code here!
for i in range (1, n+1):
    for j in range (i+1, n+1):
        for k in range (m):
            cnt_val = 0
            for x1, x2 in pairs:
                if x1 == i and x2 ==j:
                    cnt_val+=1
                elif x1==j and x2==i:
                    cnt_val+=1
        max_val = max(cnt_val, max_val)
print(max_val)                    
