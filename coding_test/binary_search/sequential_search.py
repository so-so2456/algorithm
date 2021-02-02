# 원소 갯수와 찾으려는 target을 입력하고
# array를 입력한 뒤, target의 위치를 반환

# 순차 탐색의 시간복잡도 >> O(N)
"""
5 d
a b c d e

>> 4
"""

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

input_data = input.split()
n = int(input_data[0])
target = input_data[1]

array = input.split()

print(sequential_search(n, target, array))