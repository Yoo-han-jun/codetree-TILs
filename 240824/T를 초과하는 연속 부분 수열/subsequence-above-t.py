n,t = map(int,input().split())
arr = list(map(int, input().split()))
cnt = 0
ans = 1
for i in range (n-1):
    if i>=1 and arr[i]<arr[i+1]:
        cnt+=1
    else:
        cnt=1
    ans = max(cnt, ans)
if ans >= t:
    print(ans)
else:
    print(0)