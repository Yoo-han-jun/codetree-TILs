x, y = map(int,input().split())
sum_val = 0
arr = []
for i in range (x, y+1):
    arr.append(tuple(map(int,list(str(i)))))
for i in range (len(arr)):
    cnt_val = 0
    for j in range (len(arr[i])):
        cnt_val += arr[i][j]
    sum_val = max(cnt_val, sum_val)
print(sum_val)