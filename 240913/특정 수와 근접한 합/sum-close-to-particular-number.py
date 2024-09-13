s, n = map(int,input().split())
arr = list(map(int,input().split()))
sum_val = 10000000000
for i in range (s):
    for j in range(i+1, s):
        for k in range (j+1, s):
            for l in range (k+1, s):
                cnt = arr[i]+arr[j]+arr[k]+arr[l]
                min_val = abs(cnt-n)
                sum_val = min(min_val, sum_val)
print(sum_val)