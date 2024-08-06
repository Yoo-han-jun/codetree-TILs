n = int(input())
arr = list(map(int,input().split()))
def f(arr, n):
    for i in range (1, n+1, 2):
        arr2 = []
        for j in range (0,i):
            arr2.append(arr[j])
            arr2.sort()
        print(arr2[i//2],end=" ")
f(arr,n)