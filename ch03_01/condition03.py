# 나머지 연산자를 활용한 짝수 홀수 구분

# 입력 받기
number = int(input("정수 입력>"))

# 짝수 조건
if number % 2 == 0:
    print("짝수입니다")

# 홀수 조건
if number % 2 == 1:
    print("홀수입니다")