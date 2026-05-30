# 딕셔너리 선언
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 출력
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient", dictionary["ingredient"]) 
# print("ingredient", dictionary["ingredient"][1]) # 리스트안에 특정값만 출력하고 싶을때
print("origin:", dictionary["origin"])
print()

# 값을 변경합니다.
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])