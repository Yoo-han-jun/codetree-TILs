n, k = map(int,input().split())
arr = [int(input()) for _ in range (n)]
arr2 = set()
for i in range (n):
    for j in range (i+1, n):
        if arr[i] == arr[j] and j-i<=k:
            arr2.add(arr[i])
if arr2:    
    print(max(arr2))
else:
    print(-1)