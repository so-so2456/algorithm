# N개 원소의 배열을 입력받고 입력받은 원소중에서 총 M번을 더해 가장 큰 수를 구하시오
# 단 한 원소당 연속으로 K번까지 더할 수 있다 (M <= K)
"""
-입력-

5 8 3
2 4 5 4 6

>> 46
"""


def find_high_number_1():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort()
    first = data[n - 1]
    second = data[n - 2]

    sum = 0
    cnt = 0
    for i in range(m):
        if (cnt != k):
            sum += first
            cnt += 1

        else:
            sum += second
            cnt = 0

    print(sum)


def find_high_number_2():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort()
    first = data[n - 1]
    second = data[n - 2]

    # 6 6 6 5 > 반복
    count = m // (k + 1) * k + m % (k + 1)

    sum = count * first
    sum += (m - count) * second

    print(sum)