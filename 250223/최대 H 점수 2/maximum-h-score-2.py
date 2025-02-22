N, L = map(int, input().split())
a = list(map(int, input().split()))
max_i = 0
# Write your code here!
# i보다 큰 수가 i+L개
for i in range (100):
    cnt1 = 0
    cnt2 = 0
    for j in range (N):
        if a[j]+1==i:
            cnt1+=1
        elif a[j]>=i:
            cnt2+=1
    max_num = min(cnt1, L)
    if cnt2>=i:
        max_i = max(max_i, i)
    elif cnt2+max_num>=i:
        max_i = max(max_i, i)
print(max_i)
