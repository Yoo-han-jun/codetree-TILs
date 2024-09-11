arr = [list(map(int,input().split())) for _ in range(19)]
def in_range(x, y):
    return x<19 and x>=0 and y<19 and y>=0
ans = False
a_x, a_y = 0, 0
for i in range(2, 16):
    for j in range(2,16):
        cnt1, cnt2, cnt3 =0 ,0, 0
        for k in range (-2, 3):
            if arr[i][j] ==1 or arr[i][j]==2:
                if arr[i][j] == arr[i+k][j-k]:
                    cnt1 +=1
                if arr[i][j] == arr[i+k][j]:
                    cnt2 +=1
                if arr[i][j] == arr[i][j+k]:
                    cnt3 +=1
            if cnt1 ==5 or cnt2 ==5 or cnt3==5:
                a_x, a_y = i,j
                ans = True
                break
if ans == True:
    print(arr[a_x][a_y])
    print(a_x+1, a_y+1)
else:
    print(0)