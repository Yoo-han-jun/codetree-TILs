a,b = map(int,input().split())
arr = []
while a>b:
    cnt = a%b
    arr.append(cnt)
    a = a//b
    if a<b:
        arr.append(a)
        break
arr.reverse()
for ele in arr:
    print(ele, end="")