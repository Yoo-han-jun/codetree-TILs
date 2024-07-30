cnt = 0
def print_n(n):
    global cnt
    cnt+=1
    if n == 0:
        cnt -=1
        print()
        return
    print(cnt, end=" ")
    print_n(n-1)
    print(cnt, end=" ")
    cnt-=1

    
    
n = int(input())
print_n(n)