class ex:
    def __init__(self,date,day,wea):
        self.date = date
        self.day = day
        self.wea = wea
def year(n):
    a,b, c = n.split("-")
    a, b, c = int(a), int(b), int(c)
    return 365*a+12*b+c

n = int(input())
arr = []
for _ in range (n):
    df = tuple(input().split())
    info = ex(df[0],df[1],df[2])
    arr.append(info)
cnt = year(arr[0].date)
num = 0
for i in range (0, n):
    if arr[i].wea == "Rain":
        if cnt > abs(year(arr[i].date)):
            cnt = abs(year(arr[i].date))
            num = i
print(arr[num].date, arr[num].day, arr[num].wea)