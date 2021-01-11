# 숫자가 적힌 카드들이 N x M으로 놓여 있다
# 뽑고자 하는 행을 선택하고 그 중 가장 작은 수를 뽑느다
# 그중 가장 높은 숫자를 구하시오
"""
3 3 
3 1 2
4 1 4
2 2 2
"""
n, m = map(int, input().split())
min_value = 0

for i in range(n):
    data = list(map(int, input().split()))
    tmp = min(data)
    min_value = max(min_value, tmp)

print(min_value)