n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
max_cnt = 1000000000000000
# Write your code here!
for i in range (0, 101, 2):
    for j in range (0, 101, 2):
        cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
        for k in range (n):
            if points[k][0]>i and points[k][1]>j:
                cnt1+=1
            if points[k][0]>i and points[k][1]<j:
                cnt2+=1
            if points[k][0]<i and points[k][1]>j:
                cnt3+=1
            if points[k][0]<i and points[k][1]<j:
                cnt4+=1
        max_cnt = min(max_cnt, max(cnt1, cnt2, cnt3, cnt4))
print(max_cnt)