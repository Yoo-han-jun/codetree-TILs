month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
day = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

a, b, c, d = map(int,input().split())
dat = input()
cnt = 0
cnt2 = 0
for i in range (1, a):
    cnt += month[i-1]
cnt+=b
for i in range (1, c):
    cnt2 += month[i-1]
cnt2+=d

if cnt2==cnt and dat=="Mon":
    print(1)
elif (cnt2-cnt)%7 >= day.index(dat)+1:
    print(((cnt2-cnt)//7)+1)
else:
    print(((cnt2-cnt)//7))