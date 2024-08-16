a, b, c, d = map(int,input().split())
month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
day = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
n = 1
m = 1
l = 1
o = 1
cnt = 0
cnt2 = 0
while True:
    if n==a and m==b:
        break
    m+=1
    cnt+=1
    if int(month[n-1])<m:
        m=1
        n+=1

while True:
    if l==c and o==d:
        break
    o+=1
    cnt2+=1
    if int(month[l-1])<o:
        o=1
        l+=1
print(day[cnt2%7-cnt%7])