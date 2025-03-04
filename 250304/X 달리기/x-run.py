X = int(input())
att = X
# Please write your code here.
1234321
time = 0
12321
for i in range (100000):
    cnt = i*i
    if cnt>=att:
        n = i-1
        break
sum_r = n*n
if sum_r == X:
    time = 2*n-1
elif sum_r <X:
    time = 2*n-1
    att-=sum_r
    time+=att//i
    time+=1
print(time)

