n = int(input())
arr = []
for i in range (n):
    a, b = tuple(map(int, input().split()))
    arr.append((a, b))
max_t = 1
for i in range (n):
    arr2 = [0 for _ in range (1001)]
    for j in range (n):
        if i==j:
            continue
        for l in range (arr[j][0], arr[j][1]):
            arr2[l] = 1
    cnt = 0
    for k in range (len(arr2)):
        if arr2[k] ==1:
            cnt+=1
    max_t = max(cnt, max_t)
print(max_t)