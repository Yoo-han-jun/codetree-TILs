n = int(input())
arr = list(map(int, input().split()))
def s(trr):
    for ele in trr:
        if ele % 2 ==0 :
            print (ele//2,end=" ")
        else:
            print(ele,end=" ")
s(arr)