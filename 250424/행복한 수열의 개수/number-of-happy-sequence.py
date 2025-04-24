n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_num = 0
# Please write your code here.


def find(arr, n, m):
    global max_num
    for i in range (n):
        cnt = 1
        k = arr[i][0]
        for j in range (1,n):
            if k==arr[i][j]:
                cnt+=1
            else:
                k=arr[i][j]
                cnt = 1
            if cnt>=m:
                max_num+=1
                break

def find2(arr, n, m):
    global max_num
    for i in range (n):
        cnt = 1
        k = arr[0][i]
        for j in range (1,n):
            if k==arr[j][i]:
                cnt+=1
            else:
                k=arr[j][i]
                cnt = 1
            if cnt>=m:
                max_num+=1
                break
                
find(grid,n,m)
find2(grid,n,m)
print(max_num)
