board = [list(input()) for _ in range(10)]

# Please write your code here.
x_B = 0
y_B = 0
x_L = 0
y_L =0
x_R = 0
y_R = 0
for i in range (10):
    if "B" in board[i]:
        y_B = board[i].index("B")
        x_B = i
    if "L" in board[i]:
        y_L = board[i].index("L")
        x_L = i
    if "R" in board[i]:
        y_R = board[i].index("R")
        x_R = i
if x_R==x_L==x_B:
    if max(y_B,y_L)>y_R and min(y_B, y_L)<y_R:
        print(abs(y_B-y_L)+1)
    else:
        print(abs(y_B-y_L)+abs(x_B-x_L)-1)
elif y_R==y_L==y_B:
    if max(x_B,x_L)>x_R and min(x_B, x_L)<x_R:
        print(abs(x_B-x_L)+1)
    else:
        print(abs(y_B-y_L)+abs(x_B-x_L)-1)
else:
    print(abs(y_B-y_L)+abs(x_B-x_L)-1)