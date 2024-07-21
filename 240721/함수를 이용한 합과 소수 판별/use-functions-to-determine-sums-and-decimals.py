def f(a,b):
    
    s = 0
    for i in range(a,b+1):
        cnt = 0
        for j in range(2, i):
            if i%j==0:
                cnt+=1
        if cnt == 0 and (i%10 + i//10)%2==0:
            s+=1      
    return s
a, b = map(int, input().split())
print(f(a, b))