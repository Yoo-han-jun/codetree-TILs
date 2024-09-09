n = int(input())
arr = list(map(int,input().split()))
cnt_val = 0
sum_val = 0
for i in range (n):
    for j in range (i+2, n):
        cnt_val = arr[i]+arr[j]
        sum_val = max(cnt_val, sum_val)
print(sum_val)