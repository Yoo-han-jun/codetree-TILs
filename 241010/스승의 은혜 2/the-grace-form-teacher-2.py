N, B = map(int,input().split())
arr = [int(input()) for _ in range (N)]
arr.sort()
cnt = 0
for i in range (N):
    sum_val = 0
    for j in range (i):
        sumfu = sum_val
        sumfu+=arr[j]
        if sumfu>=B:
            sumfu = sum_val
            sumfu += arr[j]//2
            if sumfu>=B:
                cnt = i-1
            else:
                cnt = i
        else:
            sum_val = sumfu
print(cnt)