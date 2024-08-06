n = int(input())
arr = list(map(int, input().split()))
sum_val = arr[0]
def low(a, b):
    while b:
        a, b = b, a % b
    return a

def s(a, n):
    global sum_val
    if n==1:
        return sum_val
    sum_val = (sum_val*a[n-1])//low(sum_val, a[n-1])
    return s(a, n-1)

print(s(arr,n))