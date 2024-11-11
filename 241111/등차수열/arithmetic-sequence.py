n = int(input())
arr = tuple(map(int,input().split()))
max_cnt = 0
for k in range (min(arr),max(arr)):
    cnt  = 0
    for i in range (n):
        for j in range (i+1,n):
            if (arr[i]+arr[j])/2 == k:
                cnt+=1
    max_cnt = max(cnt, max_cnt)
print(max_cnt)