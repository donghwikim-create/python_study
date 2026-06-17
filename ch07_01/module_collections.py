from collections import Counter

words = ["사과", "바나나", "사과", "포도", "바나나", "사과"]
Counter = Counter(words)
print(Counter) # Counter({'사과': 3, '바나나': 2, '포도': 1})
