N, B = map(int,input().split())
arr = [int(input()) for _ in range (N)]
arr.sort()
cnt = 0
answer = False
for i in range (1,N+1):
    sum_val = 0
    if answer == False:
        for j in range (i):
            sumfu = sum_val
            sumfu+=arr[j]
            if sumfu>=B:
                sumfu = sum_val
                sumfu += arr[j]//2
                if sumfu>B:
                    cnt = i-1
                    answer = True
                    break
                else:
                    cnt = i
                    answer = True
                    break
            else:
                sum_val = sumfu
print(cnt)