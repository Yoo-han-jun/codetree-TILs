n = int(input())
arr = list(map(int,input().split()))
arr2 = []
for i in range (n):
    sum_diff = 0
    for j in range (n):
        sum_diff += abs(j-i) * arr[j]
    arr2.append(sum_diff)
print(min(arr2))