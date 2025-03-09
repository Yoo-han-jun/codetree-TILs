N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)
arr = [1, 2, 3]
# Please write your code here.
def win(x, y, a, b, c):
    if x==a and y==b:
        return True
    if x==b and y==c:
        return True
    if x==c and y==a:
        return True
    else:
        return False
max_cnt = 0
for i in range (3):    
    cnt = 0
    for j in range (N):
        x= a[j]
        y= b[j]
        e, f, g = arr[i//3], arr[(i+1)//3], arr[(i+2)//3]
        if win(x,y,e,f,g):
            cnt+=1
    max_cnt = max(cnt, max_cnt)

print(max_cnt)