def pr_st(n):
    if n==0:
        return
    print("* "*n,end=" ")
    print()
    pr_st(n-1)
    print("* "*n,end="  ")
    print()
n = int(input())
pr_st(n)