import json

# 딕셔너리를 json 문자열로 변환 (Serialization)
data = {"name": "User", "role": "admin"}
json_striong = json.dumps(data)
print(json_striong)