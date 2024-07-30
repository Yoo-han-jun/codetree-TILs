def pr_n(n):
    if n==0:
        return
    print(n,end=" ")
    pr_n(n-1)
    print(n,end=" ")
n= int(input())
pr_n(n)