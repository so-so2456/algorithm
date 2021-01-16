# (1 <= N <= 100,000)
# 학생의 이름과 100이하의 자연수가 입력된다

# 최대 100,000개까지 입력될 수 있으므로
# 최악의 경우 O(NlogN) 이거나 O(N)을 보장하는 알고리즘을 사용해야 함

n = int(input())

array = []

for i in range(n):
    name, score = input().split(' ')
    int(score)
    array.append((name, score))


result = sorted(array, key=lambda student: student[1])

for info in result:
    print(info[0], end=' ')