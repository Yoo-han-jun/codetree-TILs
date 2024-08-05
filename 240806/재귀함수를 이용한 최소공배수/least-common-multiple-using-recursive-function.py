sum_val =1
def low(a, b):
    cnt = 1
    if a%b==0 or b%a==0:
        return min(a,b)
    for i in range(2, max(a,b)):
        if a%i==0 and b%i==0:
            cnt*=i
    return cnt

def s(a, n):
    global sum_val
    if n==1:
        return a[0]
    if n==2:
        return sum_val
    sum_val = (sum_val * a[n-2]) // low(a[n-2], sum_val)
    return s(a, n-1)

        
n = int(input())
arr = list(map(int, input().split()))
print(s(arr,n))