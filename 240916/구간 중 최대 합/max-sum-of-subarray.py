n, k = map(int,input().split())
arr = list(map(int,input().split()))
sum_val = 0
for i in range (n-k+1):
    cnt_val = 0
    for j in range(i, i+k):
        cnt_val+=arr[j]
    sum_val = max(sum_val, cnt_val)
print(sum_val)