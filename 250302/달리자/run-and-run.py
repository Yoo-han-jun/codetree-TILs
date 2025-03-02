n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range (n):
    if A[i] == B[i]:
        continue
    elif A[i]>B[i]:
        A[i+1] += A[i]-B[i]
        cnt += A[i]-B[i]
    elif A[i]<B[i]:
        B[i+1] += B[i]-A[i]
        cnt += B[i]-A[i]
print(cnt)