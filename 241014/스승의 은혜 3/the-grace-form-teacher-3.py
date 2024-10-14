# n, b 입력
n, b = map(int, input().split())
# price_list
price_list = list()
# price_list 채우기
for _ in range(n):
    price_list.append(tuple(map(int, input().split())))

# 함수들
# discount(k)
def discount(k):
    # unpacking
    p1, p2 = price_list[k]
    # 반값으로 내려 반환
    return p1//2 + p2

# buy_max(curr_list)
def buy_max(curr_list):

    # curr_list 정렬
    curr_list.sort()

    # 최대 구입 갯수 구하기
    for i in range(1, n):
        # 예산을 넘으면
        if sum(curr_list[:i+1]) > b:
            # 현재 인덱스를 반환
            return i

# 설계
# max_cnt
max_cnt = 0

# 하나씩 반값으로 내려보는 완전탐색
for i in range(n):
    
    # merged_price_list
    merged_price_list = []

    # merged_price_list 채우기
    for j in range(n):
        # 현재 반값으로 내리는 인덱스라면
        if i == j:
            merged_price_list.append(discount(j))
        # 이외에는
        else:
            # unpacking
            p1, p2 = price_list[j]
            # 그대로 합쳐서 추가
            merged_price_list.append(p1 + p2)
    
    # max_cnt 업데이트
    max_cnt = max(max_cnt, buy_max(merged_price_list))

# 출력
print(max_cnt)