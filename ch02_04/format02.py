# 정수

output_a = "{:d}".format(52)

# 특정 칸에 출력하기

output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

# 빈칸을 0으로 채우기

output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52) 

# 출력
print("기본:", output_a)
print()

print("5칸 뒤에 출력:", output_b)
print("10칸 뒤에 출력:", output_c)

print("빈칸을 0으로 채우기", output_d) # 양수
print("빈칸을 0으로 채우기", output_e) # 음수

