# x=10
# y=2

# if x > 4:
#     if y > 2:
#         print(x*y)
# else:
#     print(x+y)

# 태어난 해 입력받고 띠 출력하는 프로그램

str_input = input("태어난 해를 입력하 주세요>")
birth_year = int(str_input)

if birth_year % 12 == 0:
    print("원숭이 띠입니다.")
elif birth_year % 12 == 1:
    print("닭 띠입니다.")
elif birth_year % 12 == 2:
    print("개 띠입니다.")
elif birth_year % 12 == 3:
    print("돼지 띠입니다.")
elif birth_year % 12 == 4:
    print("쥐 띠입니다.")
elif birth_year % 12 == 5:
    print("소 띠입니다.")
elif birth_year % 12 == 6:
    print("범 띠입니다.")
elif birth_year % 12 == 7:
    print("토끼 띠입니다.")
elif birth_year % 12 == 8:
    print("용 띠입니다.")
elif birth_year % 12 == 9:
    print("뱀 띠입니다.")
elif birth_year % 12 == 10:
    print("말 띠입니다.")
elif birth_year % 12 == 11:
    print("양 띠입니다.")