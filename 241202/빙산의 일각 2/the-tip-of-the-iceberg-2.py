n = int(input())
arr = list()
max_t = 0
for _ in range (n):
    arr.append(int(input()))
for i in range (max(arr)):
    cnt = list()
    cnt2 = list()
    for j in range (n):
        if arr[j]>=i:
            cnt.append(1)
        else:
            cnt.append(0)
    for k in range(n-1):
        if cnt[k] !=cnt [k+1]:
            cnt2.append(cnt[k])
        if k==n-2:
            cnt2.append(cnt[n-1])
    max_t = max(cnt2.count(1), max_t)
print(max_t)