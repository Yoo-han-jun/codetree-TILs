N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
max_cnt=0
# Write your code here!
for i in range (1, 1000):
    cnt_val = 0 
    for j in range (N):
        if arr[j]>=i and arr[j]<=i+K:
            cnt_val+=1
    max_cnt = max(cnt_val, max_cnt)
print(max_cnt)
