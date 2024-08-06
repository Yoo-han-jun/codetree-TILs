n = int(input())
arr = list(map(int,input().split()))
arr.sort()
cnt = 0
for i in range(1, n+1):
    if cnt < arr[2*n-i]+arr[i-1]:
        cnt = arr[2*n-i]+arr[i-1]
print(cnt)