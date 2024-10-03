n = int(input())
class b:
    def __init__(self, number, right, guess):
        self.number = number
        self.right = right
        self.guess = guess
guess_number = []
for _ in range (n):
    number, right, guess = tuple(input().split())
    guess_number.append(b(number, right, guess))
t =guess_number[1]
total_val = 0
for i in range (1, 10):
    for j in range (1, 10):
        for k in range (1, 10):
            if i!=j and j!=k and k!=i:
                cnt_val = 0
                for l in range (n):
                    b, c = 0, 0
                    t = guess_number[l]
                    if i==int(t.number[0]):
                        b+=1
                    if j==int(t.number[1]):
                        b+=1
                    if k==int(t.number[2]):
                        b+=1
                    if i==int(t.number[1]) or i==int(t.number[2]):
                        c+=1
                    if j==int(t.number[0]) or j==int(t.number[2]):
                        c+=1
                    if k==int(t.number[1]) or k==int(t.number[0]):
                        c+=1
                    if int(t.right)==b and int(t.guess)==c:
                        cnt_val+=1
                if cnt_val ==4:
                    total_val+=1
print(total_val)