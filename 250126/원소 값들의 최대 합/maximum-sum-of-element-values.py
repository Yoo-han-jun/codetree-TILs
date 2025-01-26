n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Write your code here!
max_cnt = 0
for i in range (n):
    cnt_val = 0
    j = i
    for _ in range (m):
        cnt_val += arr[j]
        j = arr[j]
    max_cnt = max(max_cnt, cnt_val)
print(max_cnt)
