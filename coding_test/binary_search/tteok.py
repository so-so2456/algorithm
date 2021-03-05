# 떡의 개수 N과 최소한으로 받을 총 떡의 길이 M을 입력받고
# 각 떡의 길이를 입력 받는다
# 손님이 받는 떡은 잘린 길이로 받는다
# 손님이 적어도 M만큼을 얻으려면 최대 몇으로 떡을 잘라야 하는지 구하시오 

# 전형적인 이진 탐색 문제이고, 파라메트릭 서치 유형의 문제이다
# 파라메트릭 서치는 최적화 문제를 결정 문제로 바꾸어 해결하는 방법이다

# 파라메트릭 서치 유형은 이진 탐색을 재귀적이 아닌 
# 반복문을 이용해 구현하면 간결하다
"""
4 6
19 15 10 17

>> 15
"""
def search(rice_cakes, start, end, m):
    while start <= end:
        sum = 0
        mid = (start + end) // 2
        for i in rice_cakes:
            sum += i - mid if i - mid > 0 else 0
        if sum < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))
long = max(rice_cakes)
print(search(rice_cakes, 0, long, m))
