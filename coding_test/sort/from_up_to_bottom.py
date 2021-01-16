# (1 <= N <= 500)
# 1 이상 100,000 이하의 자연수가 입력된다

# 아무 정렬을 사용해도 상관없음

array = []
n = int(input())

for i in range(n):
    m = int(input())
    array.append(m)

array.sort(reverse=True)

for i in array:
    print(i, end=' ')