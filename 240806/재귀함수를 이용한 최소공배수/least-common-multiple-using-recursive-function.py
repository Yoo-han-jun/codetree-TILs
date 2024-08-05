sum_val =1
def iso(n):
    cnt=0
    for i in range (2,n-1):
        n-1%i==0
        cnt+=i
    if cnt ==0:
        return True
    else:
        return False
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
        return sum_val
    sum_val = (sum_val * a[n-1]) // low(a[n-1], sum_val)
    return s(a, n-1)

        
n = int(input())
arr = list(map(int, input().split()))
print(s(arr,n))