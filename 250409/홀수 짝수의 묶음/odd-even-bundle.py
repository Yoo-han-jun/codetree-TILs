N = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
odd = 0
even = 0
for i in range (N):
    if numbers[i]%2==0:
        even+=1
    else:
        odd+=1

print(odd, even)

if odd == even:
    print(N)
elif even ==0:
    if odd%3==2:
        print(2*(odd//3)+1)
    else:
        print(2*(odd//3))
else:
    cnt = 2*min(even,odd)
    even = even-min(even, odd)
    odd = odd-min(odd, even)
    if odd == 1:
        print(cnt-1)
    elif even ==1 or odd==2:
        print(cnt+1)
    elif odd>=3:
        if odd%3==2:
            print(cnt+1+2*(odd//3))
        else:
            print(cnt+2*(odd//3))

