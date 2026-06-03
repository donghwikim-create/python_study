# number = [103, 52, 273, 32, 77]

# print(min(number))
# print(max(number))
# print(sum(number))

# # 리스트 따로 저장하지 않고 숫자를 나열해도 최솟값, 최대값을 구할 수 있음

# print(min(103, 52, 273)) 
# print(max(103, 52, 273))

# ---

# temp = reversed([1, 2, 3, 4, 5, 6])

# for i in temp:
#     print("첫 번쨰 반복문: {}".format(i))

# for i in temp:
#     print("두 번쨰 반복문: {}".format(i))

# # 코드를 실행하면 첫 번째 반복문은 출력이 되지만
# # 두번째 반복문은 출력되지않음
# # 그 이유는 reversed() 함수는 제너레이터 이기 때문이다.

# # ---

# # 확장 슬라이싱

# numbers = [1, 2, 3, 4, 5]

# print(numbers)

# print(numbers[::-1])

# # 비파괴적 코드 이므로 원본 numbers에는 영향이 없다.

# print("안녕하세요"[::1])

# ---

# example_list = ["요소A", "요소B", "요소C"]
# i = 0

# for item in example_list:
#     print("{}번째 요소는 {}입니다.".format(i, example_list))
#     i+=1

# print()

# for i in range(len(example_list)):
#     print("{}번째 요소는 {}입니다.".format(i, example_list))

# ---    

# sample_list = [1, 3, 4, 5]

# print(sample_list.enumerate())

# sample_dict = {
#     "name": "디티오",
#     "class": "인파이터"
# }

# print(items(sample_dict))

# 리스트 내포 --> 리스트 이름 = [ 표현식 for 반복자 in 반복할 수 있는 것 if 조건문 ]
# 리스트에서 특정 문자열이 포함된 것만 출력하고 싶을때 count 함수 사용 
output = [numbers_with_one_zero_in_binary for numbers_with_one_zero_in_binary in range(1, 101) 
          if "{:b}".format(numbers_with_one_zero_in_binary).count("0") == 1] 

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))

# for i in range(1, 101):
#     print(i)
