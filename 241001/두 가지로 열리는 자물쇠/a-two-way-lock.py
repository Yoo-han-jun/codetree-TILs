n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

def f(a, b):
    if abs(a-b) <=2:
        return True
    if abs(max(a,b)-min(a,b)-n)<=2:
        return True
    else:
        return False
cnt=0
for i in range (1,n+1):
    for j in range (1,n+1):
        for k in range (1,n+1):
            if f(arr1[2],k) or f(arr1[1],j) or f(arr1[0],i):
                if f(arr2[2],k) or f(arr2[1],j) or f(arr2[0],i):
                    cnt+=1
print(n*n*n-cnt)