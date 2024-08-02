def f(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n==2:
        return 2
    return n * f(n-1)
n = int(input())
print(f(n))