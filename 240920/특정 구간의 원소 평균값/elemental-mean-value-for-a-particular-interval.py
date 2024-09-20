n = int(input())
arr = list(map(int,input().split()))
cnt = 0 
for i in range (n):
    for j in range (i, n):
        sum_val = 0
        for k in range (i, j+1):
            sum_val += arr[k]
            cnt_val = j-i+1
        if sum_val % cnt_val == 0:
            avr_val = int(sum_val / cnt_val)
            answer = False
            for k in range (i, j+1):
                if avr_val == arr[k]:
                    answer = True
            if answer == True:
                cnt+=1
print(cnt)