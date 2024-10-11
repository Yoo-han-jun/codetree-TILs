n, m, d, s = map(int,input().split())
eat = [tuple(map(int,input().split())) for _ in range (d)]
sick = [tuple(map(int,input().split())) for _ in range (s)]
# 썩은 치즈 구하기 
sick_person = set()
suck_bread = [[] for _ in range (51)]
sick.sort(key = lambda x:x[0])
for i in range (s):
    sick_person.add(sick[i][0])

for i in range (d):
    if eat[i][0] in sick_person:
        for j in range (s):
            if eat[i][0] == sick[j][0]:
                if eat[i][2]<=sick[j][1]:
                   suck_bread[eat[i][0]].append(eat[i][1]) 

non_empty_lists = [set(lst) for lst in suck_bread if lst]

# 첫 번째 리스트를 교집합으로 시작
if non_empty_lists:
    intersection = non_empty_lists[0]
    
    # 나머지 리스트와 교집합 계산
    for s in non_empty_lists[1:]:
        intersection &= s  # intersection = intersection.intersection(s)
else:
    intersection = set()  # 모든 리스트가 빈 경우

for i in range (d):
    if eat[i][0] not in sick_person:
        if eat[i][1] in intersection:
            sick_person.add(eat[i][0])

print(len(sick_person))