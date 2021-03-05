# 고유한 번호가 적혀 있는 부품 N개 중 고객이 M개를 구매하려고 한다 
# 고객이 요청한 (고유한 번호가 적힌) 부품이 있는지 확인
"""
5
8 3 7 9 2
3
5 7 9

>> no yes yes
"""
# 이진 탐색으로 푸는 법
def binary_search(parts, start, end, target):
    while start <= end:
        middle = (start + end) // 2
        if target == parts[middle]:
            return True
        elif target > parts[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return False


n = int(input())
parts = list(map(int, input().split()))
parts.sort()
m = int(input())
requests = list(map(int, input().split()))

for target in requests:
    flag = binary_search(parts, 0, n - 1, target)
    if flag:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 계수 비교로 푸는 법
n = int(input())
flag = [0] * 1000001
for idx in input.split:
    flag[int(idx)] = 1
m = int(input())
requests = list(map(int, input().split()))

for target in requests:
    if flag[target] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 집합 자료형으로 푸는 법
# 단순한 특정 데이터가 존재하는지 검사할 때 효과적임
n = int(input())
parts = set(map(int, input().split()))
m = int(input())
requests = list(map(int, input().split()))

for target in requests:
    if target in parts:
        print('yes', end=' ')
    else:
        print('no', end=' ')