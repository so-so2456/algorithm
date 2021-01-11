# 00:00:00 ~ N:59:59 동안 숫자 3이 들어가는 시각의 모든 경우의 수
# 왼전 탐색
# 하루는 86,400초로 경우의 수가 100,000개도 되지 않음
# 보통 데이터 개수가 100만 개 이하일 때 완전 탐색을 사용한다
"""
5
>> 11475
"""

n = int(input())
cnt = 0
for hour in range(n + 1):
    for min in range(60):
        for sec in range(60):
            time = f"{hour}:{min}:{sec}"
            if '3' in time:
                cnt += 1
print(cnt)