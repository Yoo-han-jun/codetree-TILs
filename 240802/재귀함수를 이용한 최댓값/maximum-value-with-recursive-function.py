n = int(input())
arr = list(map(int, input().split()))
rm = 0
def f(ar , n):
    global rm
    if rm <= ar[n-1]:
        rm = ar[n-1]
    if n == 1:
        return rm

    return f(ar, n-1)
    
print(f(arr, n))