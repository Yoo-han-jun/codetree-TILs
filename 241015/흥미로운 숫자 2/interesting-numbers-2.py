x, y = map(int,input().split())
sum_val = 0
for i in range (x, y+1):
    number = list(map(int,list(str(i))))
    cnt0 = 0
    cnt1 = 0
    arr3 = dict.fromkeys(number)
    if len(arr3) ==2:
        arr2 = list(arr3)
        for j in range (len(number)):
            if arr2[0] == number[j]:
                cnt0 +=1
            elif arr2[1] == number[j]:
                cnt1 +=1
    if cnt0 == len(number)-1 or cnt1 == len(number)-1:
        sum_val +=1
print(sum_val)