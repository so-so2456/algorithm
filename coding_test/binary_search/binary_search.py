# 이진탐색의 시건복잡도 >> O(logN)]
# 탐색범위가 2000만을 넘어가면 이진 탐색으로 문제를 접근하기

# 재귀함수
def binary_search(array, target, start, end):
    # 배열 내에 target이 없을 때
    if start > end:
        return None
    # 중간 인덱스
    middle = (start + end) // 2
    # target과 중간 값이 같으면 return
    if target == array[middle]:
        return middle
    # target이 더 크면 오른쪽 탐색
    elif target > array[middle]:
        return binary_search(array, target, middle + 1, end)
    # target이 더 작으면 왼쪽 탐색
    else:
        return binary_search(array, target, start, middle - 1)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result is None:
    print(f'There is no {target}')
else:
    print(result + 1)


# 반복문으로도 구현 가능
def binary_search_(array, target, start, end):
    while start <= end:
        middle = (start + end) // 2
        if target == array[middle]:
            return middle
        elif target > array[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return None