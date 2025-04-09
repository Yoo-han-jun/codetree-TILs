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


if even>odd:
    print(odd*2+1)
elif odd == even:
    print(odd+even)
else:
    cnt = even * 2
    k = odd - even

    if k%3==0:
        cnt+=(k//3)*2
    else:
        if((k%3)%2==0):
            cnt+= 2*(k//3)+1
        else:
            cnt+=2*(k//3)-1
    print(cnt)