n, b = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]

# 각 학생의 선물 총 가격 (가격 + 배송비) 계산
total_costs = [(p + s, p, s) for p, s in arr]

# 선물 총 가격 기준으로 정렬
total_costs.sort()

# 최대 몇 명에게 선물을 줄 수 있는지 계산
max_students = 0
current_budget = 0

for i in range(n):
    # 현재 학생에게 선물을 줄 때 필요한 비용
    total_price, p, s = total_costs[i]
    
    # 현재 예산에 이 학생의 선물을 추가할 수 있는지 확인
    if current_budget + total_price <= b:
        current_budget += total_price
        max_students += 1
    else:
        break

# 반값 쿠폰을 사용하여 최대 학생 수를 다시 계산
for i in range(n):
    # 반값 쿠폰을 사용할 경우, 해당 학생의 가격을 절반으로 줄임
    discount_price = total_costs[i][1] // 2 + total_costs[i][2]
    temp_budget = current_budget - (total_costs[i][0] if i < max_students else 0) + discount_price

    # 예산을 초과하지 않으면 최대 학생 수 갱신
    if temp_budget <= b:
        max_students = max(max_students, max_students + (1 if i >= max_students else 0))

print(max_students)