# 사용자에게 2개의 숫자를 입력받고 사칙연산(덧셈, 뺼셈, 곱셈, 나눗셈) 한 값을 출력하는 코드를 작성하시오.

input_a = int(input("첫번쨰 숫자를 입력하시오:"))
input_b = int(input("두번째 숫자를 입력하시오:"))

print("두 숫자의 합:", input_a + input_b)
print("두 숫자의 차:", input_a - input_b)
print("두 숫자의 곱:", input_a * input_b)
print("두 숫자를 몫", input_a / input_b) # 소수점이 있는 몫
print("두 숫자를 몫", input_a // input_b) # 소수점이 없는 몫
