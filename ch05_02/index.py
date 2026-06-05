# def flatten(data):
#     result = []
#     for item in data:
#         # 요소가 리스트(또는 튜플 등)라면 재귀 호출
#         if isinstance(item, list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result

# complex_list = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# print(flatten(complex_list)) # 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ---

min_table_people = 2
max_table_people = 10
total_people = 100
memo = {}

def count_table_combinations(remain_people, sit_people):
    key = str([remain_people, sit_people])
    
    # 1. 종료 조건 (기저 조건)
    if key in memo:
        return memo[key]  # 이미 계산한 적이 있다면 저장된 값을 바로 반환 (중복 계산 방지)
    if remain_people < 0:
        return 0          # 사람을 넘치게 배정한 경우이므로 무효(0가지)
    if remain_people == 0:
        return 1          # 정확히 100명을 다 채운 경우이므로 올바른 방법 1가지 발견!

    # 2. 재귀 처리
    count = 0
    # 중복을 피하기 위해 현재 테이블에는 '직전 테이블 인원(sit_people)'부터 '최대 인원(max_table_people)'까지 앉힐 수 있습니다.
    for i in range(sit_people, max_table_people + 1):
        # i명을 앉히고 남은 인원(remain_people - i)을 다음 재귀로 넘깁니다. 
        # 이때 다음 테이블은 최소 i명 이상 앉아야 하므로 i를 함께 넘깁니다.
        count += count_table_combinations(remain_people - i, i)

    # 3. 메모화 처리
    memo[key] = count     # 현재 상태(남은 인원, 현재 앉힌 인원)의 결과를 딕셔너리에 저장

    # 4. 종료
    return count          # 최종 계산된 경우의 수를 반환

print(count_table_combinations(total_people, min_table_people))