n,t = map(int,input().split())
arr = list(map(int, input().split()))
cnt = 1
ans = 1
for i in range (n-1):
    if arr[i]>t and arr[i+1]>t:
        cnt+=1
    else:
        cnt=1
    ans = max(cnt, ans)
print(ans)