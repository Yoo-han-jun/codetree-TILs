n, m = map(int, input().split())
arr = list(map(int, input().split()))
wifi = []
cnt = 0
# Please write your code here.
for i in range (n):
    if m==0:
        break
    elif arr[i]==0:
        continue
    elif arr[i]==1:
        if i in wifi:
            continue
        else:
            wifi.extend(list(range(i, i+2*m+1)))
            cnt+=1
if m==0:
    print(arr.count(1))
else:
    print(cnt)