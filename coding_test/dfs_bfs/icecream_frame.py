# N x M의 얼음 틀에서 구멍이 뚫려있는 부분은 0, 막힌 부분은 1로 표시된다
# 얻을 수 있는 총 아이스크림의 수를 툴력
"""
4 5
00110
00011
11111
00000

>> 3

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

>> 8
"""
n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 범위를 벗어나면 종료
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 2
        # 상, 하, 좌, 우
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1
print()
for i in range(n):
    for j in range(m):
        print(graph[i][j], end='')
    print()
print(result)
