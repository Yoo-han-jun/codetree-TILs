cnt = 0
def f(n):
    global cnt
    cnt+=1
    if n == 1 :
        return cnt
    if n%2==0:
        return f(n//2)
    else:
        return f(n//3)
        
n = int(input())
print(f(n)-1)