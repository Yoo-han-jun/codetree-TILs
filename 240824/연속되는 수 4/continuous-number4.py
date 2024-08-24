n = int(input())
arr = []
for _ in range(n):
    s = int(input())
    arr.append(s)
ans=1
cnt=1
for i in range (n-1):
    if arr[i]<arr[i+1]:
        cnt+=1
    else:
        cnt=1
    ans = max(cnt, ans)
print(ans)