# 기호 붙여 출력하기

output_a = "{:+d}".format(52) # 양수
output_b = "{:+d}".format(-52) # 음수
output_c = "{: d}".format(52) # 양수: 기호부분공백
output_d = "{: d}".format(-52) # 음수: 가호부분공백

print(output_a)
print(output_b)
print(output_c)
print(output_d)