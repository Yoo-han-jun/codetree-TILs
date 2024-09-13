s, n = map(int,input().split())
arr = list(map(int,input().split()))
sum_val = 10000000000
for i in range (s):
    for j in range(i+1, s):
        cnt = sum(arr)-arr[i]-arr[j]
        min_val = abs(cnt-n)
        sum_val = min(min_val, sum_val)
print(sum_val)