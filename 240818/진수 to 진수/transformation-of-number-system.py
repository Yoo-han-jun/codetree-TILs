a, b = map(int,input().split())
n = tuple(input())
num = 0
for i in range (len(n)):
    num = num * a + int(n[i])
arr = []
cnt = 0
while True:
    if num<b:
        arr.append(num)
        break
    cnt = num%b
    arr.append(cnt)
    num = num//b
for ele in arr[::-1]:
    print(ele, end="")