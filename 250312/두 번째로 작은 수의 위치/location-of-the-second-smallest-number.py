n = int(input())
a = [0] + list(map(int, input().split()))

# Please write your code here.

diff = 1000
min_val2 = 0
for i in range (1, n+1):
    if a[i]==min(a[1:]):
        continue
    else:
        cnt_diff = a[i]-min(a[1:])
        if cnt_diff<diff:
            min_val2 = a[i]
            diff = cnt_diff
r = a.index(min_val2)
if min_val2==0:
    print(-1)
elif min_val2 in a[r+1:]:
    print(-1)
else:
    print(a.index(min_val2))