arr = list(map(int,input().split()))

def diff(i, j, k):
    sum_1 = arr[i]+arr[j]+arr[k]
    sum_2 = sum(arr)-sum_1
    return abs(sum_1-sum_2)
min_val = 10000000000
for i in range(6):
    for j in range (i+1, 6):
        for k in range (j+1, 6):
            min_val = min(min_val, diff(i, j, k))
print(min_val)