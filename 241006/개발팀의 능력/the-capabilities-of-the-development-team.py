arr = list(map(int,input().split()))
n =5
def diff(i, j, k):
    if i==j or j==n or k==i:
        return 100
    else:
        return max(i, j, k) - min(i, j, k) 

min_val = 6000
for i in range(n):
     for j in range(i+1, n):
        for k in range (n):
            if i==k or j==k:
                continue 
            else:
                l = arr[i] + arr[j]
                m = arr[k]
                s = sum(arr)-l-m
                min_val = min(min_val, diff(l, m, s))

if min_val == 100:
    print(-1)
else:
    print(min_val)