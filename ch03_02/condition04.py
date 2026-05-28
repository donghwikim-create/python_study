# if조건문에 else 구문을 추가해서 짝수와 홀수 구분

# 입력을 받습니다.
number = int(input("정수 입력>"))

# 조건문 사용
if number % 2 == 0:
    # 조건이 참일 때, 즉 짝수 조건
    print("짝수입니다")
else:
    print("홀수입니다")