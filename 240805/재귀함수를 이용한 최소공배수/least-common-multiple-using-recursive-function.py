n = int(input())
arr = list(map(int, input().split()))
arr2 = []
def f(arr, n):
    global arr2
    if n==0:
        return
    for i in range (2, arr[n-1]):
        if arr[n-1]%i==0:
            arr2.append(i)
    return f(arr, n-1)        



f(arr, n)
sum_val = 1
for ele in set(arr):
    sum_val *= ele
for ele in arr2:
    sum_val = sum_val//ele
print(sum_val)