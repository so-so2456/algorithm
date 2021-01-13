# 매번 가장 작은 것을 선택해 앞 데이터와 바꾸는 것을 반복
# 선택정렬의 시간복잡도 = O(N^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)