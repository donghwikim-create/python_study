# ★★★★★★★★★★★★★★★★★★★★★★★★★★

# pets = [
#     { "name": "구름", "age": 5 },
#     { "name": "초코", "age": 3 }
# ]

# print(pets)

# for pet in pets:
#     print(pet["name"],"{}살".format(pet["age"]))

#

# ------------방법1

# numbers = [1, 2, 3, 4, 1, 1, 5, 1, 6]

# # 1. 빈 딕셔너리 생성
# result_dict = {}

# # 2. 리스트를 돌며 개수 세기
# for number in numbers:
#     if number in result_dict:
#         result_dict[number] += 1  # 이미 있다면 개수 +1
#     else:
#         result_dict[number] = 1   # 처음 나왔다면 1로 초기화

# print(result_dict)
# # 출력: {1: 4, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}

# # ---- 방법2 실무에서 많이 사용

# numbers = [1, 2, 3, 4, 1, 1, 5, 1, 6]
# result_dict = {}

# for num in numbers:
#     # num이 없으면 0을 가져오고, 거기에 1을 더해서 저장함
#     result_dict[num] = result_dict.get(num, 0) + 1

# print(result_dict)
# # 출력: {1: 4, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}

character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    value = character[key]
    
    # 1. 값이 리스트일 경우 (skill 등)
    if isinstance(value, list):
        for item in value:
            print(f"{key}: {item}")
            
    # 2. 값이 딕셔너리일 경우 (items 등)
    elif isinstance(value, dict):
        for sub_value in value.values():
            print(f"{key}: {sub_value}")
            
    # 3. 그 외 일반 값일 경우 (name, level)
    else:
        print(f"{key}: {value}")