n, m = map(int,input().split())
arr1 = [0]*1000000
arr2 = [0]*1000000
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
signs = [1 if x > 0 else -1 if x < 0 else 0 for x in result]
signs2 = [x for x in signs if x != 0]
for i in range (1,len(signs2)):
    if signs2[i]!=signs2[i-1]:
        cnt2+=1
print(cnt2)