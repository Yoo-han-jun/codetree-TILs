n, b = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]

# 선물 가격 + 배송비로 정렬
arr.sort(key=lambda x: x[0]//2 + x[1])

max_students = 0

# 선물 하나에 쿠폰을 적용하는 경우를 계산
for i in range(n):
    total_cost = 0
    count = 0

    # 모든 학생에게 선물을 줄 때 쿠폰을 i번째 선물에 적용
    for j in range(n):
        if j == i:
            # i번째 선물에만 쿠폰 적용 (가격을 반값으로 줄임)
            total_cost += arr[j][0] // 2 + arr[j][1]
        else:
            # 나머지 선물은 정상 가격으로 계산
            total_cost += arr[j][0] + arr[j][1]

        # 예산을 초과하면 종료
        if total_cost > b:
            break
        count += 1

    # 최대로 선물 가능한 학생 수를 업데이트
    max_students = max(max_students, count)

print(max_students)