n = int(input())
cnt = 100
cnt2 = 0
arr = [0]*200
for _ in range (n):
    a, b = tuple(input().split())
    a = int(a)
    if b=="R":
        for i in range(cnt, cnt+a):
            arr[i]+=1
        cnt = cnt+a
    else:
        for i in range(cnt-1,cnt-a-1,-1):
            arr[i]+=1
        cnt = cnt-a
for ele in arr:
    if ele>=2:
        cnt2+=1
print(cnt2)