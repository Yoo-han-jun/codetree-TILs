n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x, y):
    if x<=n-1 and x>=0 and y>=0 and y<=m-1:
        return True
    else:
        return False

# 가로 3개, 세로2, 가로1
def search_num1(x, y, arr, sum_num):
    if in_range(x, y) and in_range(x, y+1) and in_range(x, y+2):
        sum_num = arr[x][y] + arr[x][y+1] + arr[x][y+2]
    return sum_num
def search_num2(x, y, arr, sum_num2):
    if in_range(x, y) and in_range(x+1, y) and in_range(x+1, y+1):
        sum_num2 = arr[x][y]+ arr[x+1][y]+arr[x+1][y+1]
    return sum_num2
max_num= 0
for i in range (n):
    for j in range (m):
        sum_num = 0
        sum_num2 = 0
        print(i, j)
        print(search_num1(i, j, arr, sum_num))
        print(search_num2(i, j, arr, sum_num2))
        max_num = max(max_num, search_num1(i, j, arr, sum_num), search_num2(i, j, arr, sum_num2))
print(max_num)
            