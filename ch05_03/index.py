# # join 함수 사용할때는 문자열만 사용가능하여 map 함수를 사용해 문자열로 바꾼 후 join 함수 돌리기

# numbers = [1, 2, 3, 4, 5, 6]

# print("::".join(map(str, numbers)))

# # ---

numbers = list(range(1, 10+1)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("# 홀수만 추출하기")
print(list(filter(lambda x: x%2 ==1 , numbers)))
print()

print("# 3이상 7 미만 추출하기")
print(list(filter(lambda x: 3<=x<7, numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x: x**2 < 50,numbers)))