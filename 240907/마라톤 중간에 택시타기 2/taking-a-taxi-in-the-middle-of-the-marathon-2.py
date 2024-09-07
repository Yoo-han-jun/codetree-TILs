n = int(input())
arr = [[0, 0] for _ in range (n)]
for i in range (n):
    a, b = map(int, input().split())
    arr[i][0], arr[i][1] = a,b

sum_val = 0
total_dis = 0
for i in range (n-1):
    total_dis += abs(arr[i+1][0]-arr[i][0])+abs(arr[i+1][1]-arr[i][1])
result_dis = total_dis
for j in range (1, n-1):
    cnt_val = 0
    sum_val = 0
    cnt_val= abs(arr[j+1][0]-arr[j][0])+abs(arr[j+1][1]-arr[j][1])+ abs(arr[j-1][0]-arr[j][0])+ abs(arr[j-1][1]-arr[j][1])-abs(arr[j-1][1]-arr[j+1][1])-abs(arr[j+1][0]-arr[j-1][0])
    cnt_val = total_dis -cnt_val
    result_dis = min(cnt_val, result_dis)
print(result_dis)