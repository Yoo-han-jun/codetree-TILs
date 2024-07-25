n = int(input())
arr = list(map(int, input().split()))
def ab(arr):
    brr = []
    for ele in arr:
        brr.append(abs(ele))
    for ele in brr:
        print(ele, end=" ")
ab(arr)