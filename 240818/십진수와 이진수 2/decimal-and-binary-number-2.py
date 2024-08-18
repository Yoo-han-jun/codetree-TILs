n = tuple(input())
num = 0
for i in range (len(n)):
    num = num*2+int(n[i])
num *= 17
arr=[]
cnt = 0
while True:
    if num<2:
        arr.append(num)
        break
    cnt = num % 2 
    arr.append(cnt)
    num = num//2
for ele in arr[::-1]:
    print(ele, end="")