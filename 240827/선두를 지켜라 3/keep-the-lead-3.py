a, b = map(int,input().split())
arra=[0]*100
arrb=[0]*100
num = 0 
num2= 0
cnt = 0
for _ in range (a):
    v, t= map(int,input().split())
    for _ in range (t):
        arra[num+1] = arra[num] + v
        num+=1
    cnt +=t
for _ in range (b):
    v, t= map(int,input().split())
    for _ in range (t):
        arrb[num2+1] = arrb[num2] + v 
        num2+=1
result = [a-b for a, b in zip (arra, arrb)]
result2 = []
for i in range (cnt):
    if result[i] <0:
        result2.append(-1)
    elif result[i] ==0:
        result2.append(0)
    elif result[i] >0:
        result2.append(1)
cnt2=0
for i in range (cnt-1):
    if result2[i] != result2[i+1]:
        cnt2+=1
print(cnt2)