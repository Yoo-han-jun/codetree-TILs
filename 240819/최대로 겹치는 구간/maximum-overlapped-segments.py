n = int(input())
arr = [0]*201
for _ in range(n):
    a, b= map(int,input().split())
    a += 100
    b += 100
    for i in range(a+1, b):
        arr[i]+=1

print(max(arr))