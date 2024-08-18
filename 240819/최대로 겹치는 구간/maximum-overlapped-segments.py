n = int(input())
arr = [0]*210
for _ in range(n):
    a, b= map(int,input().split())
    a += 101
    b += 101
    for i in range(a, b):
        arr[i]+=1

print(max(arr))