x, y = map(str, input().split())
a, b = int(x), int(y)
cnt = 0
for i in range (a, b+1):
    c = list(str(i))
    error = 0
    if len(c)%2==0:
        for j in range (len(c)):
            if c[j] != c[len(c)-j-1]:
                error+=1
            if j == len(c)-j-1:
                break
    if len(c)%2==1:
        del c[len(c)//2]
        for j in range (len(c)):
            if c[j] != c[len(c)-j-1]:
                error+=1
            if j == len(c)-j+2:
                break
    if error == 0 :
        cnt+=1
print(cnt)


    