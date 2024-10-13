n, b = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range (n)]
arr.sort(key = lambda x:(x[0]+x[1], x[1]))
sum_val = 0
for i in range (n):
    p, d = arr[i]
    predict_val = sum_val+p+d
    if predict_val>= b:
        predict_val = sum_val + p//2+d
        if predict_val >=b:
            print(i)
        else:
            sum_val = predict_val
    sum_val = predict_val