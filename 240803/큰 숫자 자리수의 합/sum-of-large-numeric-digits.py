def f(n):
    if n<10:
        return n
    return f(n//10) + n%10

arr = list(map(int,input().split()))
val = 1
for ele in arr:
    val *= ele

print (f(val))