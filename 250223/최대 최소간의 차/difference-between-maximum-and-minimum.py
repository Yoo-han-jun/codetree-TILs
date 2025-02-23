n, k = map(int, input().split())
arr = list(map(int, input().split()))
max_cnt = 10000000
# 최대 최소 K
for i in range (100):
    cnt = 0
    for j in range (n):
        if arr[j]>i+k:
            cnt+=abs(i+k-arr[j])
        elif arr[j]<i:
            cnt+=abs(arr[j]-i)
    max_cnt = min(max_cnt, cnt)

print(max_cnt)
    
# Write your code here!