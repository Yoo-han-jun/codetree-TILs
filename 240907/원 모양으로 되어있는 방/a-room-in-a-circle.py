n = int(input())
arr=[]
for _ in range(n):
    r = int(input())
    arr.append(r)
result = 1000000000000000000000000000
for i in range(n):
    sum_p = sum(arr)
    cnt_val = 0
    for j in range (i, 2*n):
        if j>=n:
            j = j%n
        sum_p -= arr[j]
        if sum_p==0:
            break
        cnt_val+=sum_p 
    result = min(result, cnt_val)
print(result)