n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = -10000000
for i in range (n):
    for j in range (i+1, n):
        for k in range (j+1, n):
            cbt = arr[i] * arr[j] * arr[k]
        cnt = max(cnt, cbt)
print(cnt)