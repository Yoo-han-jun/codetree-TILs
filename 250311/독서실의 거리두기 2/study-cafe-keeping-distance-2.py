N = int(input())
seats = input()
# Please write your code here.
def find_large_seat(N):
    arr1 = []
    for i in range (len(N)):
        if int(N[i])==1:
            arr1.append(i)      
    return arr1

def find_biggest_seat_current(N):
    arr2 = []
    for i in range (len(N)-1):
        arr2.append(N[i+1]-N[i])
    return min(arr2)

def find_biggest_seat(N):
    arr2 = []
    for i in range (len(N)-1):
        arr2.append(N[i+1]-N[i])
    return arr2.index(max(arr2))

arr1 = find_large_seat(seats)
biggest = find_biggest_seat(find_large_seat(seats))
max_val = 0
if arr1[biggest+1]-arr1[biggest] <= 2:
    print(0)
else:
    for j in range (arr1[biggest]+2, arr1[biggest+1]-1):
        arr2 = arr1.copy()
        arr2.append(j)
        arr2.sort()
        max_val = max(max_val, find_biggest_seat_current(arr2))
    arr2 = arr1.copy()
    arr2.append(N-1)
    max_val = max(max_val, find_biggest_seat_current(arr2))
print(max_val)