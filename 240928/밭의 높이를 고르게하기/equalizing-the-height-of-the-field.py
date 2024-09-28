N, H, T = map(int,input().split())
# N개의 밭 / H 높이 / 최소 T번
arr = list(map(int, input().split()))
arr2 =[]
for i in range (N):
    arr2.append(abs(arr[i]-H))
min_val = 1000000
for i in range(N-T+1):
    cnt_val = 0
    for j in range (i, i+T):
        cnt_val += arr2[j]
    min_val = min(cnt_val, min_val)
print(min_val)