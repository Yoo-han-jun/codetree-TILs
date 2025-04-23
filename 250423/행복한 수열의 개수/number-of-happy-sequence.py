n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_num = 0
# Please write your code here.
def find(arr, n, m, d):
    for i in range (n):
        cnt = 1
        n = arr[i][0]
        for j in range (1,n):
            if n==arr[i][j]:
                cnt+=1
                if cnt>=m:
                    d+=1
                    continue
            else:
                n=arr[i][j]
                cnt = 1

def find2(arr, n, m, d):
    for i in range (n):
        cnt = 1
        n = arr[0][i]
        for j in range (1,n):
            if n==arr[j][i]:
                cnt+=1
                if cnt>=m:
                    d+=1
                    continue
            else:
                n=arr[j][i]
                cnt = 1

find(grid, n, m, max_num)
find2(grid, n, m, max_num)
print(max_num)