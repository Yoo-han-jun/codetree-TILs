N = int(input())
heights = [int(input()) for _ in range(N)]
min_cnt=1000000
# Write your code here!
for i in range (1, 101):
    cnt = 0
    for j in range (N):
        if heights[j]<=i :
            cnt+=(heights[j]-i)*(heights[j]-i)
        elif heights[j]>=i+17:
            cnt+=(heights[j]-i-17)*(heights[j]-i-17)
    min_cnt = min(min_cnt, cnt)
print(min_cnt)