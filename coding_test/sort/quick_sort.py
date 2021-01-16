# 기준 데이터(피벗)을 설정하고
# 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈
#
# 퀵 정렬은 피벗을 설정하고
# 리스트를 분할하는 방법에 따라서
# 여러가지 방식이 있음
#
# 호어 분할 방식
# 리스트에서 첫 번째 데이터를 피벗으로 정함
# 퀵 정렬의 시간 복잡도 = O(NlogN)
# (단, 이미 데이터가 정렬되어 있는 경우에 시간복잡도는 O(N^2)이다)

# 비슷한 정렬 알고리즘: 병합 정렬

# 부등호 유의

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)


"""
# 파이썬만의 퀵 정렬
# 코드가 직관적이나 기존 퀵 정렬보단 비효율적임

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


array = quick_sort(array)
print(array)
"""