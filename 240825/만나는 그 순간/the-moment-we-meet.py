n, m = map(int, input().split())
arra = [0]*50
arrb = [0]*50
cnt = 0
number = 0
cnt2 =0
number2 =0
for i in range (n):
    d, t = tuple(input().split())
    t = int(t)
    if d == "R":
        for _ in range (t):
            number+=1
            cnt+=1
            arra[number] = cnt
    else:
        for _ in range (t):
            number+=1
            cnt-=1
            arra[number] = cnt
for i in range (m):
    d, t = tuple(input().split())
    t = int(t)
    if d == "R":
        for _ in range (t):
            number2+=1
            cnt2+=1
            arrb[number2] = cnt2
    else:
        for _ in range (t):
            number2+=1
            cnt2-=1
            arrb[number2] = cnt2

cnt3 = 0
for i in range (1, max(number,number2)):
    if arra[i] == arrb[i]:
        print(i)
        break
    else:
        cnt3+=1
if cnt == max(number,number2)-1:
    print(-1)