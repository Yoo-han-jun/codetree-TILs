arr = list(map(int,input().split()))
n = 6
arr.sort()
sum_val = sum(arr)
team1 = arr[5]+arr[0]
team2 = arr[4]+arr[1]
team3 = arr[3]+arr[2]
print(abs(max(team1, team2, team3)-min(team1,team2,team3)))