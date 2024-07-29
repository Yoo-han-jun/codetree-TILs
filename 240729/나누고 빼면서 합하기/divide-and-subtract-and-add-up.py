n, m = map(int,input().split())
arr = list(map(int,input().split()))
def s(arr, m):
    sum_val = 0
    while (m>=1):
        sum_val += arr[m-1]
        m = m//2
    return sum_val
print(s(arr, m))