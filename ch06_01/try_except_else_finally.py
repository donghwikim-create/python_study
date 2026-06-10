import math

# try except 구문으로 예외를 처리합니다.
try:
    # 숫자를 변환합니다.
    radius = int(input("정수 입력> "))
except:
    print("정수를 입력하지 않았습니다. 정수를 입력하세요.")
else:
    circumference = 2 * math.pi * radius
    area = math.pi * radius * radius
    print("원의 반지름:", radius)
    print("원의 둘레:", circumference)
    print("원의 넓이(area): ", area)
finally:
    print("마지막에 무조건 실행되는 출력문 입니다.")