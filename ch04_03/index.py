# 3. 기존의 빈 딕셔너리에 for문으로 넣기
# 처음에 가지고 계시던 빈 딕셔너리 변수(character = {})를 
# 꼭 그대로 유지하면서 값을 채워 넣어야 하는 상황이라면, enumerate()나 인덱스를 활용할 수 있습니다.

# key_list = ["name", "hp", "mp", "level"]
# value_list = ["기사", 200, 30, 5]
# character = {}

# # 인덱스(i)를 활용해서 하나씩 매칭하며 넣기
# for i in range(len(key_list)):
#     character[key_list[i]] = value_list[i]

# print(character)

# limit = 10000
# sum_value = 0  # 합계를 저장할 변수
# i = 1     # 1씩 증가시킬 숫자 변수

# # 합계가 1000 이하인 동안 계속 반복
# while sum_value <= limit:
#     i += 1          # 숫자를 1씩 증가 (1, 2, 3, ...)
#     sum_value += i  # 증가한 숫자를 합계에 더함

# print("{}를 더할 때 {}를 넘으면 그때의 값은 {}입니다.".format(i-1, limit, sum_value))

max_value = 0
a = 0
b = 0

for i in range(99, 0, -1):
    j = 100 - i
    current_product = j * i

    # 현재 곱한 값이 기존 최대값보다 크다면 업데이트
    if current_product > max_value:
        max_value = current_product
        a, b = i, j

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))

