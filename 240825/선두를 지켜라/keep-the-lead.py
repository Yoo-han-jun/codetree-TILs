n, m = map(int,input().split())
arr1 = [0]*50
arr2 = [0]*50
num1 = 1
cnt = 0
num2 =1
cnt2 = 0
for _ in range (n):
    v, t = map(int,input().split())
    for _ in range(t):
        arr1[num1] = arr1[num1-1] + v
        num1+=1
    cnt+=t
for _ in range (m):
    v, t = map(int,input().split())
    for _ in range (t):
        arr2[num2] = arr2[num2-1] + v
        num2+=1
result = [a - b for a, b in zip(arr1, arr2)]
cnt2=0
arr3 = []
for i in range (cnt):
    if result[i]<0:
        arr3.append(-1)
    if result[i]>0:
        arr3.append(1)
    if result[i]==0:
        arr3.append(0)
for i in range (cnt):
    if arr3[i] ==0:
        arr3[i] = arr3[i-1]
for i in range (cnt):
    if arr3[i]!=arr3[i-1]:
        cnt2+=1
print(cnt2)