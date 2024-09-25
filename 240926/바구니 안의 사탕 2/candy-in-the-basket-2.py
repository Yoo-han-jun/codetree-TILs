n, k = map(int,input().split())
arr = [0 for _ in range (101)]
for _ in range(n):
    a, b = map(int,input().split())
    arr[b] += a
sum_val = 0
for i in range (100):
    cnt_val = 0
    if i+k+1>=100:
        for j in range (max(0, i-k), 101):
            cnt_val += arr[j]
    else:
        for j in range (max(0, i-k), i+k+1):
            cnt_val += arr[j]
    sum_val = max(sum_val, cnt_val)
print(sum_val)