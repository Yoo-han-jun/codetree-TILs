def pr(s):
    if s<10:
        return s*s
    return pr(s//10)+pr(s%10)

n = int(input())
print(pr(n))