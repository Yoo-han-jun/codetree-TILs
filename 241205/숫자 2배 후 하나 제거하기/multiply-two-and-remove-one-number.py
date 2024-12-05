n = int(input())
min_val = 100000000000000
arr = list(map(int,input().split()))
for j in range (n):
    re_arr = [ele*2 if k==j else ele for k, ele in enumerate(arr)]
    for m in range (n):
        cnt = 0
        re_re_arr = [ele for k, ele in enumerate(re_arr) if k!=m]
        for l in range (len(re_re_arr)-1):
            cnt += abs(re_re_arr[l]-re_re_arr[l+1])
        min_val = min(cnt, min_val)
print(min_val)