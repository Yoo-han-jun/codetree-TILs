n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
def is_possible(max_val, k):
    arr_possible = []
    for i, ele in enumerate (arr):
        if ele <= max_val:
            arr_possible.append(i)
    
    #arr size
    arr_size = len(arr_possible)
    if arr_size ==0:
        return False
    for i in range (1, arr_size):
        dis = arr_possible[i]-arr_possible[i-1]
        if dis >k:
            return False

    return True

max_num = 1000 
for i in range (101, max(arr[0], arr[-1])-1, -1):
    if is_possible(i, k):
        max_num = min(i, max_num)
print(max_num)