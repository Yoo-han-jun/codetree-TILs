a, b, x, y = map(int, input().split())

# Please write your code here.

distance = b-a
distance2 = abs(min(a, b)- min(x,y))+abs(max(a,b)-max(x,y))

distance = min(distance, distance2)
print(distance)