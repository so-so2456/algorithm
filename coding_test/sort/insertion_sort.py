# 데이터를 하나씩 확인하여, 각 데이터를 적절한 위치에 삽입
# 데이터가 거의 정렬 되어 있을 때 효율적임
# 삽입정렬의 시간복잡도 = O(N^2)
# (단, 데이터가 거의 정렬된 상태라면 O(N)을 가짐)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
