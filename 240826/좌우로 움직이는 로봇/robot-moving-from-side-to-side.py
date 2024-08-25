n, m = map(int,input().split())
Max_R = 1000000
arra = [0]*50
arrb = [0]*50
numa = 0
numb = 0
disa = 0
disb = 0
cnta = 0
cntb = 0
for _ in range (n):
    t, d = tuple(input().split())
    t= int(t)
    if d == "R":
        for _ in range (t):
            numa+=1
            disa+=1
            arra[numa] = disa
        cnta+=t
    else:
        for _ in range (t):
            numa+=1
            disa-=1
            arra[numa] = disa
        cnta+=t
for _ in range (m):
    t, d = tuple(input().split())
    t= int(t)
    if d == "R":
        for _ in range (t):
            numb+=1
            disb+=1
            arrb[numb] = disb
        cntb+=t
    else:
        for _ in range (t):
            numb+=1
            disb-=1
            arrb[numb] = disb
        cntb+=t
arra[cnta:max(cnta,cntb)] = [disa] * (max(cnta,cntb)-cnta)
arrb[cntb:max(cnta,cntb)] = [disb] * (max(cnta,cntb)-cntb)

cnt = 0
result = [a-b for a,b in zip (arra, arrb)]
for i in range (1, max(cnta,cntb)):
    if result[i] !=0 and result[i+1] ==0:
        cnt+=1
print(cnt)